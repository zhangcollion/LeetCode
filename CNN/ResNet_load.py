import torch
import torch.nn as nn
import torch.nn.functional as F 
from torchvision import models


def ResNet(nn.Module):
    def __init__(self, base_model_name, pretrained=True, num_class=264): #out_channels=[64,128,256,512,1024]
        super(ResNet, self).__init__()
        base_model = models.__getattribute__(base_model_name)(pretrained=pretrained)
        layers = list(base_model.children())[:-2]
        layers.append(nn.AdaptiveMaxPool2d(1))
        self.encoder = nn.Sequential(*layers)

        in_features = base_model.fc.in_features
        self.classifier = nn.Sequential(
            nn.Linear(in_features, 1024), nn.ReLU(), nn.Dropout(p=0.2),
            nn.Linear(1024,1024), nn.ReLU(), nn.Dropout(p=0.2),
            nn.Linear(1024, num_class))

    def forward(self, x):
        batch_size = x.size(0)
        x = self.encoder(x).view(batch_size, -1)
        x = self.classifier(x)
        multiclass_prob = F.softmax(x, dim=1)
        multilabel_prob = F.sigmoid(x)
        return {
                "logits":x,
                "multiclass_prob":multiclass_prob,
                "multilabel_prob":multilabel_prob
        }