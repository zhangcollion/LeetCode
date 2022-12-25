import torch
import torch.nn as nn
import torchvison


class SimSiam(nn.Module):
    def __init__(self, base_model, dim):
        super(SimSiam, self).__init__()
        self.encoder_f = base_model
        self.encoder_q = base_model

        mlp = self.encoder_f.fc.weight.shape[1]
        self.encoder_f_proj = nn.Sequential(self.encoder_f.fc, nn.BatchNorm1d(), nn.Linear(mlp,dim))
        self.encoder_q_proj = nn.Sequential(self.encoder_q.fc, nn.BatchNorm1d(), nn.Linear(mlp,dim))

        self.encoder_f_pred = nn.Sequential(nn.Linear(dim,512), nn.BatchNorm1d(), nn.Linear(512,2048))


    def encode_weight_update(self):
        for para_f, para_q in zip(self.encoder_f.parameters(), self.encoder_q.parameters()):
            para_f.data.copy_(para_q.data)

    def proj_weight_update(self):
        for para_f, para_q in zip(self.encoder_f_proj.parameters(), self.encoder_q_proj.parameters()):
            para_f.data.copy_(para_q.data)


    def forward(self, x1, x2):
        x1 = self.encoder_f(x1)
        x2 = self.encoder_q(x2)

        x1 = self.encoder_f_proj(x1)
        x2 = self.encoder_q_proj(x2)

        p1 = self.encoder_f_pred(x1)

        return p1, x2


def calc_loss(p1, z2):
    z2 = z2.detach()
    p1 = F.normalize(p1, dim=1)
    z2 = F.normalize(z2, dim=1)
    loss = -(p1*z2).sum(dim=1).mean()

    return loss
    

optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1)







