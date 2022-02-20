from torchvision import transforms, datasets
from autoaugment import RandAugment
import torch_geometric.nn as pyg_nn
import torch_geometric.utils as pyg_utils


class GNNStack(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, task='node'):
        super(GNNStack, self).__init__()
        self.task = task
        self.convs = nn.ModuleList()
        self.convs.append(self._build_conv_model(input_dim, hidden_dim))
        for i in range(2):
            self.convs.append(self._build_conv_model(hidden_dim, hidden_dim))

        self.post_mp = nn.Sequential(nn.Linear(hidden_dim, hidden_dim), nn.Dropout(0.25),
                                    nn.Linear(hidden_dim, output_dim))

        if not (self.task == 'node'  or self.task == 'graph'):
            raise RuntimeError("Unknown task")

        self.dropout = 0.25
        self.num_layers = 3

    def _build_conv_model(self, input_dim, hidden_dim):
        if self.task == 'node':
            return pyg_nn.GCNConv(input_dim, hidden_dim)
        else:
            return pyg_nn.GINConv(nn.Sequential(nn.Linear(input_dim, hidden_dim)), 
                                  nn.ReLU(), nn.Linear(hidden_dim, hidden_dim))

    def forward(self, data):
        # edge_index is adjacency matrix
        # adjacency matrix主要告诉图中结点的连接关系，以便于计算交互特征
        x, edge_index, batch = data.x, data.edge_index, data.batch
        if data.num_node_features == 0:
            x = torch.ones(data.num_nodes, 1)

        for i in range(self.num_layers):
            x = self.convs[i](x, edge_index)
            emb = x
            x = F.relu(x)
            x = F.dropout(x, p=self.dropout, training=self.training)

        if self.task == 'graph':
            x = pyg_nn.global_mean_poll(x, batch)
        x = self.post_mp(x)

        return emb, F.log_softmax(x, dim=1)

    def loss(self, pred, label):
        return F.nll_loss(pred, label)

from tensorboardX import SummaryWriter
writer = SummaryWriter("./log/" + "filename")

def  train(dataset,task,writer):

    model = GNNStack(max(dataset.num_nodes,1), 32, dataset.num_classes, task=task)
    opt = optim.Adam(model.parameters(), lr=0.01)

    for epoch in range(200):
        total_loss = 0
        model.train()
        for batch in loader:
            opy.zero_grad()
            embedding, pred = model(batch)
            label = batch.y
            if task == 'node':
                pred = pred[batch.train_mask]
                label = label[batch.train_mask]
            loss = model.loss(pred, label)
            loss.backward()
            opt.step()
            total_loss += loss.item() * batch.num_graphs

        total_loss /= len(loader.dataset)
        writer.add_scalar("loss", total_loss, epoch)

        if epoch%10 == 0:
            writer.add_scalar("test accuracy", test_acc, epoch)

    return model
 

def CustomConv(pyg_nn.MseeagePassing):
    def __init__(self, in_channels, out_channels):
        super(CustomConv,self).__init__(aggr='add')
        self.lin = nn.Linear(in_channels, out_channels)
        self.lin_self = nn.Linear(in_channels, out_channels)

    def forward(self, x, edge_index):
        edge_index, _ = pyg_utils.remove_self_loops(edge_index)

        self_x = self.lin_self(x)

        return self_x + self.propagate(edge_index, size=(x.size(0), x.size(0)), x=self.lin(x))

    def message(self, x_i, x_j, edge_index, size):
        row, col = edge_index
        deg = pyg_utils.degree(row, size[0], dtype=x_j.dtype)
        deg_inv_sqrt = deg.pow(-0.5)
        norm = deg_inv_sqrt[row] * deg_inv_sqrt[col]
        return x_j

    def update(self, aggr_out):
        return aggr_out








