import torch
import torch.nn as nn
from torch.nn import Sequential as Seq, Linear, Relu
from torch_geometric.nn import MessagePassing
from torch_geometric.utils import remove_self_loops, add_self_loops
import torch_geometric.nn as pyg_nn
import torch_geometric.utils as pyg_utils

class GraphAttentionLayer(nn.Module):

    def __init__(self, in_features, out_features, dropout=0.6, alpha=0.2, concat=True):
        super().__init__()
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

    def forward(self, h):
        Wh = torch.bmm(h, self.W)
        a_input = self._prepare_attentional_mechanism_input(Wh)
        e = self.leakyrelu(torch.matmul(a_input, self.a).squeeze(3))

        attention = F.softmax(e, dim=1)
        attention = F.dropout(attention, self.dropout, training=self.training)
        h_prime = torch.bmm(attention, Wh)

        if self.concat:
            return F.elu(h_prime)
        else:
            return h_prime

    def _prepare_attentional_mechanism_input(self, Wh):
        B, N, D = Wh.shape
        Wh_repeated_in_chunks = Wh.repeat_interleave(N, dim=1)
        Wh_repeated_alternating = Wh.repeat(1, N, 1)

        all_combinations_matrix = torch.cat([Wh_repeated_in_chunks, Wh_repeated_alternating], dim=2)
        return all_combinations_matrix.view(-1, N, N, 2 * D)

    def __repr__(self):
        return self.__class__.__name__+'('+str(self.in_features)+'->'+str(self.out_features)+')'




class GATPairClassifier(nn.Module):
    def __init__(self, nfeat, nhid=8, nclass=1, dropout=0.6, alpha=0.2, nheads=8, pooling='first'):
        super().__init__()
        self.dropout = dropout
        self.pooling = pooling

        ## 多头attention
        self.attentions = [GraphAttentionLayer(nfeat, nhid, dropout=dropout, alpha=alpha, concat=True) 
                            for _ in range(nheads)]
        for i, attention in enumerate(self.attentions):
            self.add_module('attention_{}'.format(i), attention)

        self.out_att = GraphAttentionLayer(nhid * nheads, nhid, dropout=dropout, alpha=alpha, concat=False)

        self.classifier = nn.Sequential(
            nn.Linear(nfeat + nhid, nhid),
            nn.PReLU(),
            nn.BatchNorm1d(nhid),
            nn.Linear(nhid, nclass),
        )

    def forward_gat(self, x):
        x = F.dropout(x, self.dropout, training=self.training)
        x = torch.cat([att(x) for att in self.attention], dim=2)
        x = F.dropout(x, self.dropout, training=self.training)
        x = F.elu(self.out_att(x))
        if self.pooling == 'first':
            return x[:, 0]
        else:
            return x.mean(dim=1)

    def forward(self, feats, neighbor_feats):
        gat_feats = self.forward_gat(neighbor_feats)
        cat_feats = torch.cat([feats, gat_feats],dim=1)
        return self.classifier(cat_feats).squeeze(1)