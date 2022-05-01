import os

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from tensorboardX import SummaryWriter
from network import actor, critic, Q_net
from torch.distributions import Normal


class SAC():
    def __init__(self, args, state_dim, action_dim, device, Transition, max_action, min_val):
        super(SAC, self).__init__()
        self.device = device
        self.args = args
        self.Transition = Transition
        self.max_action = max_action
        self.min_val = min_val
        self.policy_net = actor.Actor(state_dim, max_action).to(device)
        self.value_net = critic.Critic(state_dim).to(device)
        self.Q_net = Q_net.Q(state_dim, action_dim).to(device)
        self.target_value_net = critic.Critic(state_dim).to(device)

        self.replay_buffer = [Transition] * args.capacity
        self.policy_optimizer = optim.Adam(self.policy_net.parameters(), lr=args.learning_rate)
        self.value_net_optimizer = optim.Adam(self.value_net.parameters(), lr=args.learning_rate)
        self.value_loss = nn.MSELoss()
        self.Q_net_optimizer = optim.Adam(self.Q_net.parameters(), lr=args.learning_rate)
        self.Q_criterion = nn.MSELoss()

        self.num_transition = 0
        self.num_training = 1
        self.writer = SummaryWriter('./exp_SAC')

        for target_parmas, params in zip(self.target_value_net.parameters(), self.value_net.parameters()):
            target_parmas.data.copy_(params.data)

        os.makedirs("./SAC_model", exist_ok=True)

    def select_action(self, state):
        state = torch.FloatTensor(state).to(self.device)
        mu, log_sima = self.policy_net(state)
        sigma = torch.exp(log_sima)
        dist = Normal(mu, sigma)
        z = dist.sample()
        action = torch.tanh(z).detach().cpu().numpy()
        return action.item()

    def store(self, s, a, r, s_, d):
        index = self.num_transition % self.args.capacity
        transition = self.Transition(s, a, r, s_, d)
        self.replay_buffer[index] = transition
        self.num_transition += 1

    def get_action_log_prob(self, state):
        batch_mu, batch_log_sigma = self.policy_net(state)
        batch_sigma = torch.exp(batch_log_sigma)
        dist = Normal(batch_mu, batch_sigma)
        z = dist.sample()
        action = torch.tanh(z)
        log_prob = dist.log_prob(z) - torch.log(1 - action.pow(2) + self.min_val) #logpi(a|s)
        return action, log_prob, z, batch_mu, batch_log_sigma

    def update(self):
        if self.num_training % 500 == 0:
            print("Training .....{} ".format(self.num_training))
        s = torch.tensor([t.s for t in self.replay_buffer]).float().to(self.device)
        a = torch.tensor([t.a for t in self.replay_buffer]).float().to(self.device)
        r = torch.tensor([t.r for t in self.replay_buffer]).float().to(self.device)
        s_ = torch.tensor([t.s_ for t in self.replay_buffer]).float().to(self.device)
        d = torch.tensor([t.d for t in self.replay_buffer]).float().to(self.device)

        for _ in range(self.args.gradient_steps):
            index = np.random.choice(range(self.args.capacity), self.args.batch_size, replace=False)
            bn_s = s[index]
            bn_a = a[index].reshape(-1, 1)
            bn_r = r[index].reshape(-1, 1)
            bn_s_ = s_[index]
            bn_d = d[index].reshape(-1, 1)

            target_value = self.target_value_net(bn_s_)
            next_q_value = bn_r + (1 - bn_d) * self.args.gamma * target_value
            excepted_q = self.Q_net(bn_s, bn_a)

            Q_loss = self.Q_criterion(excepted_q, next_q_value.detach())
            Q_loss = Q_loss.mean()  #J_Q

            excepted_value = self.value_net(bn_s)
            sample_action, log_prob, z, batch_mu, batch_log_sigma = self.get_action_log_prob(bn_s)
            excepted_new_Q = self.Q_net(bn_s, sample_action)
            next_value = excepted_new_Q - log_prob
            v_loss = self.value_loss(excepted_value, next_value.detach())
            v_loss = v_loss.mean()  #J_V

            log_policy_target = excepted_new_Q - excepted_value
            pi_loss = log_prob * (log_prob-log_policy_target).detach()
            pi_loss = pi_loss.mean()

            self.writer.add_scalar('Loss/V_loss', v_loss, global_step=self.num_training)
            self.writer.add_scalar('Loss/Q_loss', Q_loss, global_step=self.num_training)
            self.writer.add_scalar('Loss/pi_loss', pi_loss, global_step=self.num_training)

            self.value_net_optimizer.zero_grad()
            v_loss.backward(retain_graph=True)
            nn.utils.clip_grad_norm_(self.value_net.parameters(), 0.5)
            self.value_net_optimizer.step()

            self.Q_net_optimizer.zero_grad()
            Q_loss.backward(retain_graph=True)
            nn.utils.clip_grad_norm_(self.Q_net.parameters(), 0.5)
            self.Q_net_optimizer.step()

            self.policy_optimizer.zero_grad()
            pi_loss.backward(retain_graph=True)
            nn.utils.clip_grad_norm_(self.policy_net.parameters(), 0.5)
            self.policy_optimizer.step()

            for target_param, param in zip(self.target_value_net.parameters(), self.value_net.parameters()):
                target_param.data.copy_(target_param*(1-self.args.tau)+param*self.args.tau)

            self.num_training += 1

    def save(self):
        torch.save(self.policy_net.state_dict(), './SAC_model/policy_net.pth')
        torch.save(self.value_net.state_dict(), './SAC_model/value_net.pth')
        torch.save(self.Q_net.state_dict(), './SAC_model/Q_net.pth')

        print("====================================")
        print("Model has been saved...")
        print("====================================")

    def load(self):
        torch.load(self.policy_net.state_dict(), './SAC_model/policy_net.pth')
        torch.load(self.value_net.state_dict(), './SAC_model/value_net.pth')
        torch.load(self.Q_net.state_dict(), './SAC_model/Q_net.pth')
        print("==============Model has been loaded...======================")

