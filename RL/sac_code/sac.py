import argparse
import os
import gym
from collections import namedtuple
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Normal
from tensorboardX import SummaryWriter
from agent import sac_agent

## 参数定义
device = "cuda" if torch.cuda.is_available() else "cpu"
parser = argparse.ArgumentParser()

parser.add_argument("--env_name", default="Pendulum-v0")
parser.add_argument("--tau", default=0.005, type=float)
parser.add_argument("--target_update_interval", default=1, type=int)
parser.add_argument('--gradient_steps', default=1, type=int)

parser.add_argument('--learning_rate', default=3e-4, type=int)
parser.add_argument('--gamma', default=0.99, type=int)  # discount gamma
parser.add_argument('--capacity', default=10000, type=int)  # replay buffer size
parser.add_argument('--iteration', default=2000, type=int)  # num of  games
parser.add_argument('--batch_size', default=128, type=int)  # mini batch size
parser.add_argument('--seed', default=1, type=int)

# optional parameters
parser.add_argument('--num_hidden_layers', default=2, type=int)
parser.add_argument('--num_hidden_units_per_layer', default=256, type=int)
parser.add_argument('--sample_frequency', default=256, type=int)
parser.add_argument('--activation', default='Relu', type=str)
parser.add_argument('--render', default=False, type=bool)  # show UI or not
parser.add_argument('--log_interval', default=20, type=int)  #
parser.add_argument('--load', default=False, type=bool)  # load model

args, unknown = parser.parse_known_args()


## 初始化
class NormallizedAction(gym.ActionWrapper):

    def action(self, action):
        low = self.action_space.low
        high = self.action_space.high
        action = low + (action + 1.0) * 0.5 * (high - low)
        action = np.clip(action, low, high)
        return action

    def reverse_action(self, action):
        low = self.action_space.low
        high = self.action_space.high
        action = 2 * (action - low) / (high - low) - 1
        action = np.clip(action, low, high)
        return action


env = NormallizedAction(gym.make(args.env_name))
env.seed(args.seed)
torch.manual_seed(args.seed)
np.random.seed(args.seed)

state_dim = env.observation_space.shape[0]
action_dim = env.action_space.shape[0]
max_action = float(env.action_space.high[0])
min_val = torch.tensor(1e-4).float()
Transition = namedtuple("Transition", ['s', 'a', 'r', 's_', 'd'])


def main():
    agent = sac_agent.SAC(args, state_dim, action_dim, device, Transition, max_action, min_val)
    if args.load:
        agent.load()
    if args.render:
        env.render()
    print("====================================")
    print("Collection Experience...")
    print("====================================")
    ep_r = 0
    for i in range(args.iteration):
        state = env.reset()
        for t in range(200):
            action = agent.select_action(state)
            next_state, reward, done, info = env.step(np.float(action))
            ep_r += reward
            if args.render:
                env.render()
            agent.store(state, action, reward, next_state, done)

            if agent.num_transition >= args.capacity:
                agent.update()
            state = next_state
            if done or t == 199:
                if i % 10 == 0:
                    print("Ep_i {}, the ep_r is {}, the t is {}".format(i, ep_r, t))
                break
        if i % args.log_interval == 0:
            agent.save()
        agent.writer.add_scalar('ep_r', ep_r, global_step=i)
        ep_r = 0

if __name__=="__main__":
    main()