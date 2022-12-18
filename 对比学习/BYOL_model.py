import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models


class BYOLModel(self.Module):
    def __init__(self, base_model, dim=128):
        super(BYOLModel, self).__init__()
        self.online_encoder = base_model(num_classes=dim)
        self.target_encoder = base_model(num_classes=dim)
        for online_paras, target_paras in zip(self.online_encoder.parameters(),self.target_encoder.parameters()):
            online_paras.data.copy_(target_paras.data)

        dim_mlp = self.online_encoder.fc.weight.shape[1]
        self.online_proj = nn.Sequential(self.online_encoder.fc, nn.BatchNorm1d(), nn.ReLU(), nn.Linear(dim_mlp, dim_mlp))
        self.target_proj = nn.Sequential(self.target_encoder.fc, nn.BatchNorm1d(), nn.ReLU(), nn.Linear(), nn.Linear(dim_mlp, dim_mlp))

        self.online_predict = nn.Sequential(nn.Linear(dim_mlp, dim_mlp), nn.BatchNorm1d(), nn.ReLU(), nn.Linear(dim_mlp, dim_mlp))



    def forward(self, x):
        x1 = self.augment_trans1(x)
        x2 = self.augment_trans2(x)
        x1 = self.online_encoder(x1)
        x1 = self.online_proj(x1)
        x1_latent = self.online_predict(x1)

