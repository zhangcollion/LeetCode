import torch
import numpy as np
import random
# random.seed(3407)
# np.random.seed(3407)
# torch.manual_seed(3407)

def y_data(tmp_x):
    y = tmp_x ** 2
    return y


from torch.utils.data import Dataset
from torch import FloatTensor


class UserDataset(Dataset):
    def __init__(self, doc="dataset"):
        self.doc = doc
        x = list(range(0, 100, 3))
        self.x = FloatTensor(x).view(-1, 1)
        y = list(map(y_data, x))
        self.y = FloatTensor(y).view(-1, 1)

    def __getitem__(self, index):
        return self.x[index], self.y[index]

    def __len__(self):
        return len(self.x)


import torch.nn as nn


class reg_model(nn.Module):
    def __init__(self, in_dim, out_dim=1):
        super(reg_model, self).__init__()
        print(torch.initial_seed())
        self.in_dim = in_dim
        self.out_dim = out_dim
        #         self.model = nn.Sequential(nn.Linear(in_dim, 16), nn.ReLU(),nn.Linear(16, out_dim))
        self.fc1 = nn.Linear(in_dim, 16)
        self.act = nn.ReLU()
        self.fc2 = nn.Linear(16, out_dim)

    def forward(self, x):
        #         y = self.model(x)
        x = self.fc1(x)
        x = self.act(x)
        y = self.fc2(x)
        return y