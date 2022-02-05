import numpy as np
import os
from common.rollout import RolloutWorker
from agent.agent import Agents
from common.replay_buffer import ReplayBuffer
import matplotlib.pyplot as plt


class Runner:
    def __init__(self, env, args):
        self.env = env
        ## create agent according to args##
        if args.alg == "qmix":
            self.agent = Agents(args)
            self.rolloutWorker = RolloutWorker(env, self.agent, args)

        self.args = args
        self.win_rates = []
        self.episode_rewards = []
        self.buffer = ReplayBuffer(args)

        self.save_path = self.args.result_dir+'/'+args.alg+args.map
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        else:
            raise Exception("No such algorithm")

    def run(self, alg_num):
        num = alg_num
        self.num = num
        time_steps = 0
        train_steps = 0
        evaluate_steps = -1
        while time_steps < self.args.n_steps:
            print('Run {}, time {}'.format(num, time_steps))
            ## 满足模型evaluate条件，验证模型性能
            if time_steps // self.args.evaluate_cycle > evaluate_steps:
                win_rate, episode_reward = self.evaluate()
                self.win_rates.append(win_rate)
                self.episode_rewards.append(episode_reward)
                evaluate_steps += 1

            ## play self.args.n_episodes times game
            episodes = []
            for episode_idx in range(self.args.n_episodes):
                episode, _, _, steps = self.rolloutWorker.generate_episode(episode_idx)
                episodes.append(episode)
                time_steps += steps

            episode_batch = episodes[0]
            episodes.pop(0)
            for episode in episodes:
                for key in episode_batch.keys():
                    episode_batch[key] = np.concatenate((episode_batch[key], episode[key]), axis=0)

            self.buffer.store_episode(episode_batch)
            for train_step in range(self.args.train_steps):
                mini_batch = self.buffer.sample(min(self.buffer.current_size, self.args.batch_size))
                self.agent.train(mini_batch, train_steps)
                train_steps += 1
            win_rate,episode_reward = self.evaluate()
            print('win_rate is ', win_rate)
            self.win_rates.append(win_rate)
            self.episode_rewards.append(episode_reward)


    ## 模型验证: 使用训练好的模型玩几局游戏统计得分和胜利次数
    def evaluate(self):
        win_number = 0
        episode_rewards = 0
        for epoch in range(self.args.evaluate_epoch):
            _, episode_reward, win_tag, _ = self.rolloutWorker.generate_episode(epoch, evaluate=True)
            episode_rewards += episode_reward
            if win_tag:
                win_number += 1
        return win_number / self.args.evaluate_epoch, episode_rewards / self.args.evaluate_epoch





