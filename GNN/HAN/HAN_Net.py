from typing import Dict, List, Optional, Union

import torch
import torch.nn.functional as F
from torch import Tensor, nn

from torch_geometric.nn.conv import MessagePassing
from torch_geometric.nn.dense import Linear
from torch_geometric.nn.inits import glorot, reset
from torch_geometric.typing import Adj, EdgeType, Metadata, NodeType
from torch_geometric.utils import softmax


def group(xs, q, k_lin):
    ## 不同类型的meta path 有不同的注意力值
    ## sematic-level 注意力计算使用相同参数
    if len(xs) == 0:
        return None
    else:
        num_edge_types = len(xs)
        out = torch.stack(xs)
        attn_score = (q * torch.tanh(k_lin(out)).mean(1)).sum(-1)
        attn = F.softmax(attn_score, dim=0)
        out = torch.sum(attn.view(num_edge_types, 1, -1) * out, dim=0)
        return out

def HANConv(MessagePassing):
    def __init__(self, in_channels, out_channels, metadata, heads, 
                 negative_slope=0.2, dropout=0.0, **kwargs):
        super().__init__(aggr='add', node_dim=0, **kwargs)
        if not isinstance(in_channels, dict):
            in_channels  = {node_type:in_channels for node_type in metadata[0]}

        self.heads = heads
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.negative_slope = negative_slope
        self.metadata = metadata
        self.dropout = dropout
        self.k_lin = nn.Linear(out_channels, out_channels)
        self.q = nn.Parameter(torch.Tensor(1., out_channels))

        self.proj = nn.ModuleDict()
        for node_type, in_channels in self.in_channels.items():
            self.1[node_type] = Linear(in_channels, out_channels)

        self.lin_src = nn.ParameterDict()
        self.lin_dst = nn.ParameterDict()
        dim  = out_channels//heads
        for edge_type in metadata[1]:
            edge_type = "__".join(edge_type)
            self.lin_src[edge_type] = nn.Parameter(torch.Tensor(1, heads, dim))
            self.lin_dst[edge_type] = nn.Parameter(torch.Tensor(1, heads, dim))

        self.reset_parameters()

    def reset_parameters(self):
        reset(self.proj)
        glorot(self.lin_src)
        glorot(self.lin_dst)
        self.k_lin.reset_parameters()
        glorot(self.q)


    def forward(self, x_dict, edge_type_dict):
        H, D = self.heads, self.out_channels//self.heads
        x_node_dict, out_dict =  {}, {}


        ## node-level Aggregating [使用传播机制]
        # node type operate
        for node_type, x_node in x_dict.items():
            x_node_dict[node_type] = self.proj[node_type](x_node).view(-1, H, D)
            out_dict[node_type] = []

        # edge type operate
        for edge_type, edge_index in edge_index_dict.items():
            src_type, _, dst_type = edge_type
            edge_type = '__'.join(edge_type)
            lin_src = self.lin_src[edge_type]
            lin_dst = self.lin_dst[edge_type]
            x_src = x_node_dict[src_type]
            x_dst = x_node_dict[dst_type]
            
            alpha_src = (x_src*lin_src).sum(dim=-1)
            alpha_dst = (x_dst*lin_dst).sum(dim=-1)
            alpha = (alpha_src, alpha_dst)

            out = self.propagate(edge_index, x_dst=x_dst, alpha=alpha, size=None)
            out = F.relu(out)
            out_dict[dst_type].append(out)

        ## semantic-level aggregating process 
        for node_type, outs in out_dict.items():
            out = group(outs, self.q, self.k_lin)
            if out is None:
                out_dict[node_type] = None
                continue
            out_dict[node_type] = out

        return out_dict

    def message(self, x_dst_i, alpha_i, alpha_j, index, ptr, size_i):       
        alpha = alpha_j + alpha_i
        alpha = F.leaky_relu(alpha, self.negative_slope)
        alpha = softmax(alpha, index, ptr, size_i)
        alpha = F.dropout(alpha, p=self.dropout, training=self.training)
        out = x_dst_i * alpha.view(-1, self.heads, 1)
        return out.view(-1, self.out_channels)



