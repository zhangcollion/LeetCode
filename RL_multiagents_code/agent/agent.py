import numpy as np
import torch
from torch.distributions import Categorical
import torch.nn.functional as F


class Agents:
    def __init__(self, args):
        self.n_actions = args.n_actions
        self.n_agents = args.n_agents
        self.state_shape = args.state_shape
        self.obs_shape = args.obs_shape

        if args.alg == 'qmix':
            from policy.qmix import QMIX
            self.policy = QMIX(args)

        self.args = args

    def choose_action(self, obs, last_actions, agent_num, avail_actions, epsilon,
                      maven_z=None, evaluate=False):

        inputs = obs.copy()
        avail_actions_ind = np.nonzero(avail_actions)[0]

        agent_id = np.zeros(self.n_agents)
        agent_id[agent_num] = 1.0

        if self.args.last_action:
            inputs = np.hstack((inputs, last_actions))
        if self.args.reuse_network:
            inputs = np.hstack((inputs, agent_id))
        hidden_state = self.policy.eval_hidden[:, agent_num, :]

        inputs = torch.tensor(inputs, dtype=torch.float32).unsqueeze(0)
        avail_actions = torch.tensor(avail_actions, dtype=torch.float32).unsqueeze(0)
        if self.args.cuda:
            inputs = inputs.cuda()
            hidden_state = hidden_state.cuda()

        q_value, self.policy.eval_hidden[:, agent_num, :] = self.policy.eval_rnn(inputs, hidden_state)

        q_value[avail_actions == 0.0] = -float("inf")
        if np.random.uniform() < epsilon:
            action = np.random.choice(avail_actions_ind)
        else:
            action = torch.argmax(q_value)

        return action

    def _choose_action_from_softmax(self, inputs, avail_actions, epsilon, evaluate=False):

        action_num = avail_actions.sum(dim=1, keep_dim=True).float().repeat(1, avail_actions.shape[-1])
        prob = F.softmax(inputs, dim=-1)
        prob = ((1 - epsilon) * prob + torch.ones_like(prob) * epsilon / action_num)
        prob[avail_actions == 0] = 0.0

        if epsilon == 0 and evaluate:
            action = torch.argmax(prob)
        else:
            action = Categorical(prob).sample().long()

        return action

    def _get_max_episode_len(self, batch):
        terminated = batch['terminated']
        episode_num = terminated.shape[0]
        max_episode_len = 0
        for episode_idx in range(episode_num):
            for transition_idx in range(self.args.episode_limit):
                if terminated[episode_idx, transition_idx, 0] == 1:
                    if transition_idx + 1 >= max_episode_len:
                        max_episode_len = transition_idx + 1
                    break
        return max_episode_len

    def train(self, batch, train_step, epsilon=None):
        max_episode_len = self._get_max_episode_len(batch)
        for key in batch.keys():
            if key != 'z':
                batch[key] = batch[key][:, :max_episode_len]
        self.policy.learn(batch, max_episode_len, train_step, epsilon)
        if train_step > 0 and train_step % self.args.save_cycle == 0:
            self.policy.save_model(train_step)
