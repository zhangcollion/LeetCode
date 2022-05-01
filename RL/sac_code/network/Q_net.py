import  torch
import torch.nn as nn
import torch.nn.functional as F

class Q(nn.Module):
    def __init__(self, state_dim, action_dim ):
        self.state_dim = state_dim
        self.action_dim = action_dim
        super(Q, self).__init__()
        self.fc1 = nn.Linear(state_dim+action_dim,256)
        self.fc2 = nn.Linear(256, 256)
        self.fc3 = nn.Linear(256, 1)


    def forward(self, s, a):
        s = s.reshape(-1, self.state_dim)
        a = a.reshape(-1, self.action_dim)
        x = torch.cat((s, a), -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)   

        return x


        
