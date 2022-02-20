import torch
import torch.nn as nn
from torch.nn import Sequential as Seq, Linear, Relu
from torch_geometric.nn import MessagePassing
from torch_geometric.utils import remove_self_loops, add_self_loops
import torch_geometric.nn as pyg_nn
import torch_geometric.utils as pyg_utils

class SAGEConv(MessagePassing):
    def __init__(self, in_channels, out_channels):
        super(SAGEConv, self).__init__(aggr='max')
        self.lin = Linear(in_channels, out_channels)
        self.act = nn.Relu()
        self.update_lin = Linear(in_channels+out_channels, in_channels, bias=False)
        self.update_act = Relu()

    def forward(self, x, edge_index):
        # edge_index, _ = remove_self_loops(edge_index)
        edge_index, _ = add_self_loops(edge_index,num_nodes=x.size(0))
        return self.propagate(edge_index, size=(x.size(0), x.size(0)), x=x)

    def message(self, x_j):
        # x_i 为某个节点
        # x_j 为其邻近节点
        x_j = self.lin(x_j)
        x_j = self.act(x_j)
        return x_j

    def update(self, aggr_out, x):
        # aggr_out 为aggregate的输出
        # x 为传到propagate的输入，在message，aggregate, update中都可以使用
        new_embdding = torch.cat([aggr_out, x], dim=1)
        new_embdding = self.update_lin(new_embdding)
        new_embdding = self.update_act(new_embdding)

        return new_embdding











