import numpy as np 
import copy
import torch
import torch.nn as nn
import torch.nn.functional as F


device = torch.device("cuda" if torch.cuda.is_availale() else "cpu")


class Actor(nn.Module):
    def __init__(self, state_dim, action_dim, max_action):
        super(Actor, self).__init__()

        self.fc1 = nn.Linear(state_dim, 256)
        self.fc2 = nn.Linear(256,256)
        self.fc3 = nn.Linear(256,action_dim)

        self.max_action = max_action

    def forward(self, state):
        a = F.relu(self.fc1(state))
        a = F.relu(self.fc2(a))
        return self.max_action*torch.tanh(self.fc3(a))



    class Critic(nn.Module):
        def __init__(self, state_dim, action_dim):
            super(Critic, self).__init__()
            self.fc1 = nn.Linear(state_dim+action_dim,256)
            self.fc2 = nn.Linear(256,256)
            self.fc3 = nn.Linear(256,1)


            self.fc4 = nn.Linear(state_dim+action_dim,256)
            self.fc5 = nn.Linear(256,256)
            self.fc6 = nn.Linear(256,1)

        def forward(self, state, action):
            state_action = torch.cat([state, action],1)
            q1 = F.relu(self.fc1(state_action))
            q1 = F.relu(self.fc2(q1))
            q1 = self.fc3(q1)

            q2 = F.relu(self.fc4(state_action))
            q2 = F.relu(self.fc5(q2))
            q2 = self.fc6(q2)

        def Q1(self, state, action):
            state_action = torch.cat([state, action],1)
            q1 = F.relu(self.fc1(state_action))
            q1 = F.relu(self.fc2(q1))
            q1 = self.fc3(q1)


    class TD3:





        def train(self, replay_buffer, batch_size=256):
            self.total_it += 1
            state,action,next_state,reward,not_done = replay_buffer.sample(batch_size)

            with torch.no_grad():
                noise = (torch.randn_like(action) * self.policy_noise
            ).clamp(-self.noise_clip, self.noise_clip)

                next_action = (self.action_target(next_state)+noise).clamp(-self.max_action, self.max_action)

                target_Q1, target_Q2 = self.critic_target(next_state, next_action)
                target_Q = min(target_Q1,target_Q2)
                target_Q = reward + not_done * self.discount*target_Q

            current_Q1, current_Q1 = self.critic(state, action)
            critic_loss = F.mse_loss(current_Q1, target_Q1) + F.mse_loss(current_Q2, target_Q2)

            self.critic_optimizer.zero_grad()
            critic_loss.backward()
            self.critic_optimizer.step()

            if self.total_it % self.policy_freq == 0:
                actor_loss = -self.critic.Q1(state, self.actor(state)).mean()
                self.actor_optimizer.zero_grad()
                actor_loss.backward()
                self.actor_optimizer.step()

                for param, target_param in zip(self.critic.parameters(),self.critic_target.parameters()):
                    target_param.data.copy_(self.tau*param.data + (1-self.tau)*target_param.data)

                for param, target_param in zip(self.actor.parameters(), self.action_target.parameters()):
                    target_param.data.copy_(self.tau*param.data + (1-self.tau)*target_param.data)








