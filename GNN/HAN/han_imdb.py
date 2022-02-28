import os.path as osp
from typing import Dict, List, Union

import torch
import torch.nn.functional as F 
from torch import nn

import torh_geometric.transformers as T
from torh_geometric.datasets import IMDB
from torch_geometric.nn import HANConv


path = osp.join(osp.dirname(osp.realpath(__file__)), '../../data/IMDB')
metapaths = [[('movie', 'actor'), ('actor', 'movie')],
             [('movie', 'director'), ('director', 'movie')]]
transform = T.AddMetaPaths(metapaths=metapaths, drop_orig_edges=True,
                           drop_unconnected_nodes=True)
dataset = IMDB(path, transform=transform)
data = dataset[0]
print(data)


class HAN(nn.Module):
    def __init__(self, in_channels, out_channels, hidden_channels=128, heads=8):
        super(HAN, self).__init__()
        self.han_conv = HANConv(in_channels, hidden_channels, heads=heads,
                                deopout=0.6, metadata=data.metadata())
        self.lin = nn.Linear(hidden_channels, out_channels)

    def forward(self, x_dict, edge_index_dict):
        out = self.han_conv(x_dict, edge_index_dict)
        out = self.lin(out['movie'])
        return out

model = HAN(in_channels=-1, out_channels=3)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
data, model = data.to(device), model.to(device)

optimizer = torch.optim.Adam(model.parameters(),lr=0.005,weight_decay=0.001)

def train():
    model.train()
    optimizer.zero_grad()
    out = model(data.x_dict, data.edge_index_dict)
    mask = data['movie'].train_mask
    loss = F.cross_entroy(out[mask], data['movie'].y[mask])
    loss.backward()
    optimizer.step()
    return float(loss) 