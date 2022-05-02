import gym
import numpy as np

class Qlearner:
    def __init__(self, env, epsilon,alpha, gamma):
        self.N = env.observation_space.n
        self.M = env.action_space.n
        self.Q = np.zeros((self.N, self.M))
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma

    def act(self, s_t):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.M)
        else:
            return np.argmax(self.Q[s_t])

    def learn(self, s_t, a_t, r_t, s_t_next, d_t):
        a_t_next = np.argmax(self.Q[s_t_next])
        Q_target = r_t + self.gamma*(1-d_t)*self.Q[s_t_next, a_t_next]
        self.Q[s_t, a_t] = (1-self.alpha)*self.Q[s_t, a_t] + self.alpha*(Q_target)


def train(env, agent, T=1000000):
    s_t = env.reset()
    for t in range(T):
        a_t = agent.act(s_t)
        s_t_next, r_t, d_t, _ = env.step(a_t)
        agent.learn(s_t, a_t, r_t, s_t_next, d_t)
        s_t = s_t_next
        if d_t:
            s_t = env.reset()
    return agent


def valcode(env, policy, T=10000):

    policy.epsilon = 0
    scores = []
    s_t = env.reset()
    for t in range(T):
        a_t = policy.act(s_t)
        s_t, r_t, d_t, _ = env.step(a_t)
        if d_t:
            scores.append(r_t)
            env.reset()
    return sum(scores)/len(scores)


env = gym.make('FrozenLake-v0')
env.seed(0)
ql = Qlearner(env, epsilon=0.2, gamma=0.99, alpha=0.1)
ql = train(env, ql)

score = valcode(env, ql)
print('-----------', score)
print('==========', ql.Q)


