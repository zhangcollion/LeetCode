import torch
import torch.nn as nn
from torch.nn import Sequential as Seq, Linear, Relu
from torch_geometric import MessagePassing
from torch_geometric.utils import remove_self_loops, add_self_loops
import torch_geometric.nn as pyg_nn
import torch_geometric.utils as pyg_utils
from message import SAGEConv
from torch_geometric.data import Data
embed_dim = 128
from torch_geometric.nn import TopKPooling
from torch_geometric.nn import global_mean_pool as gap, global_max_pool as gmp
import torch.nn.functional as F


class gnnNet(nn.Module):
    def __init__(self):
        super(gnnNet, self).__init__()
        hidden = 128
        self.conv1 = SAGEConv(embed_dim, hidden)
        self.pool1 = TopKPooling(hidden, ratio=0.8)
        self.conv2 = SAGEConv(hidden, hidden)
        self.pool2 = TopKPooling(hidden, ratio=0.8)
        self.conv3 = SAGEConv(hidden, hidden)
        self.pool3 = TopKPooling(hidden, ratio=0.8)
        self.item_embedding = nn.Embedding(num_embeddings=df.item_id.max() +1, embedding_dim=embed_dim)
        self.lin1 = Linear(embed_dim*2, hidden)
        self.lin2 = Linear(hidden, hidden//2)
        self.lin2 = Linear(hidden//2, 1)
        self.bn1 = nn.BatchNorm1d(hidden)
        self.bn2 = nn.BatchNorm1d(hidden//2)
        self.act1 = nn.Relu()
        self.act2 = nn.Relu()

    def forward(self, data):
        x, edge_index, batch = data.x, data.edge_index, data.batch
        x = self.item_embedding(x)
        x = x.squeeze(1)

        x = F.relu(self.conv1(x, edge_index))
        x, edge_index, _, batch, _ = self.pool1(x, edge_index, None, batch)
        x1 = torch.cat([gmp(x, batch), gap(x, batch)], dim=1)

        x = F.relu(self.conv2(x, edge_index))
        x, edge_index, _, batch, _ = self.pool2(x, edge_index, None, batch)
        x2 = torch.cat([gmp(x, batch), gap(x, batch)], dim=1)

        x = F.relu(self.conv3(x, edge_index))
        x, edge_index, _, batch, _ = self.pool3(x, edge_index, None, batch)
        x3 = torch.cat([gmp(x, batch), gap(x, batch)], dim=1)

        x = x1 + x2 + x3

        x = self.lin1(x)
        x = self.act1(x)
        x = self.lin2(x)
        x = self.act2(x)
        x = F.dropout(x, p=0.5, training=self.training)

        x = torch.sigmoid(self.lin3(x)).squeeze(x)

        return x



















