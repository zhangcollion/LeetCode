import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

class NodeClassifier(nn.Module):
    def __init__(self, input_dim, num_graph_layers, hidden_dim, output_dim, dropout_pct):
        super(NodeClassifier, self).__init__()
        
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.num_graph_layers = num_graph_layers
        
        self.convs = nn.ModuleList()
        self.convs.append(GCNConv(input_dim, hidden_dim))
        for i in range(num_graph_layers-1):
            self.convs.append(GCNConv(hidden_dim, hidden_dim))
        
        self.dropout_pct = dropout_pct
        self.clf_head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.Dropout(dropout_pct),
            nn.Linear(hidden_dim, output_dim)
        )
        
        
    def forward(self, data):
        x, edge_index, batch = data.x, data.edge_index, data.batch
        
        for i in range(self.num_graph_layers):
            x = self.convs[i](x, edge_index)
            x = F.relu(x)
            x = F.dropout(x, p=self.dropout_pct)
            
        x = self.clf_head(x)
        return F.log_softmax(x, dim=1)
    
    def loss(self, pred, label):
        return F.nll_loss(pred, label)
        