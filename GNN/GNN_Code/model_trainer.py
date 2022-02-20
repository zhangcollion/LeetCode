import torch
import torch.nn as nn
from torch.nn import Sequential as Seq, Linear, Relu
from torch_geometric import MessagePassing
from torch_geometric.utils import remove_self_loops, add_self_loops
import torch_geometric.nn as pyg_nn
import torch_geometric.utils as pyg_utils
from message import SAGEConv
from model_define import gnnNet
from torch_geometric.data import Data
from torch_geometric.nn import TopKPooling
from torch_geometric.nn import global_mean_pool as gap, global_max_pool as gmp
import torch.nn.functional as F
from tensorboardX import SummaryWriter

def tarin():

    model.train()
    loss_all = 0

    for data in train_loader:
        data = data.to(device)
        optim.zero_grad()
        output = model(data)
        label = data.y.to(device)
        loss = crit(output, label)
        loss.backward()
        loss_all += data.num_graphs*loss.item()
        optim.step()

    return loss_all/len(train_dataset)

device = 'cuda' if torch.cuda.is_available else 'cpu'
model = gnnNet().to(device)
optim = torch.optim.Adam(model.parameters(), lr=0.0001)
crit = torch.nn.BCELoss()
train_loader = DataLoader(train_dataset, batch_size=batch_size)
writer = SummaryWriter()
num_epochs = 1000
for epoch in range(num_epochs):
    log_loss = train()
    writer.add_scaler("log/loss_log", log_loss, epoch)

writer.close()






















