
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch_geometric as PyG
from torch_geometric.nn import MessagePassing


class  GATLayer(nn.Module):
    def __init__(self, in_features, out_features, dropout, alpha, concat=True): 
        super(GATLayer, self).__init__
        self.dropout = dropout
        self.in_features = in_features
        self.out_features = out_features
        self.alpha = alpha
        self.concat = concat

        self.W = nn.Parameter(torch.zeros(size=(in_features, out_features)))
        nn.init.xavier_uniform_(self.W.data, gain=1.414)

        self.a = nn.Parameter(torch.zeros(size=(2*out_features, 1)))
        nn.init.xavier_uniform_(self.a.data, gain=1.414)

        self.leakyrelu = nn.LeakyRelu(self.alpha)

    def forward(self, x, edge_index):
        h = torch.mm(x, self.W)
        N = h.size()[0]

        ## Attention Mechanism
        a_input = torch.cat([h.repeat(1, N).view(N * N, -1), h.repeat(N, 1)], dim=1).view(N, -1, 2 * self.out_features)
        e = self.leakyrelu(torch.matmul(a_input, self.a).squeeze(2))

        ## Masked Attention
        zero_vec = -9e15*torch.ones_like(e)
        attention = torch.where(adj>0, e, zero_vec)

        attention = F.softmax(attention, dim=1)
        attention = F.dropout(attention, self.dropout, training=self.training)
        h_prime = torch.matmul(attention, h)

        if self.concat:
            return F.elu(h_prime)
        else:
            return h_prime