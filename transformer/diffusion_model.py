from typing import Dict, Tuple
from tqdm import tqdm
import torch
import torch.nn as nn
import torch.nn.funcitonal as F
from torch.utils.data import DataLoader
from torchvision import models, transforms
from torchvison.utils import save_image, make_grid
import matplotlib.pyplot as plt
import numpy as numpy
from diffusion_utilities import *

## hyperparameters

timesteps = 500
beta1 = 1e-4
beta2 = 0.02
device = torch.device("cuda:0" if torch.cuda.is_available() else "CPU")
n_feat = 64
n_cfeat = 5
height = 16

batch_size=100
n_epoch=32
lrate=1e-3

b_t = (beat2-beat1)*torch.linspacer(0, 1, timesteps+1, device=device)
a_t = 1 - b_t
ab_t = torch.cumsum(a_t.log(), dim=0).exp()
ab_t[0] = 1

class ContextUnet(nn.Module):
    def __init__(self, in_channels, n_feat=256, n_cfeat=10, height=28):
        super(ContextUnet, self).__init__()
        self.in_channels = in_channels
        self.n_feat = n_feat
        self.n_cfeat = n_cfeat    
        self.h = height

        self.init_conv = ResidualConvBlock(in_channels, n_feat, is_res=True)

        self.down1 = UnetDown(n_feat, n_feat)
        self.down2 = UnetDown(n_feat, 2*n_feat)

        self.to_vec = nn.Sequential(nn.AvgPool2d((4)), nn.GELU())

        self.timeembed1 = EmbedFC(1, 2*n_feat)
        self.timeembed2 = EmbedFC(1, 1*n_feat)
        self.contextembed1 = EmbedFC(n_cfeat, 2*n_feat)
        self.contextembed2 = EmbedFC(n_cfeat, 1*n_feat)

        self.up0 = nn.Sequential(
                nn.ConvTranspose2d(2*n_feat, 2*n_feat,self.h//4, self.h),
                nn.GroupNorm(8, 2*n_feat),
                nn.ReLU(),
            )
        self.up1 = UnetUp(4*n_feat, n_feat)
        self.up2 = UnetUp(2*n_feat, n_feat)

        self.out = nn.Sequential(
            nn.Conv2d(2*n_feat,n_feat,3,1,1),
            nn.GroupNorm(8, n_feat),
            nn.ReLU(),
            nn.Conv2d(n_feat, self.in_channels, 3,1,1)
            )
    def forward(self, x, t, c=None):
        x = self.init_conv(x)
        down1 = self.down1(x)
        down2= self.down2(down1)

        hiddenvec = self.to_vec(down2)
        
        if c is None:
            c = torch.zeros(x.shape[0], self.n_cfeat).to(x)

        cemb1 = self.contextembed1(c).view(-1, self.n_feat*2, 1,1)
        temb1 = self.timeembed1(t).view(-1, self.n_feat*2, 1,1)
        cemb2 = self.contextembed2(c).view(-1, self.n_feat, 1,1)
        temb2 = self.timeembed2(t).view(-1, self.n_feat, 1,1)

        up1 = self.up0(hiddenvec)
        up2 = self.up1(cemb1*up1 + temb1, down2)
        up3 = self.up2(cemb2*up2 + temb2, down1)
        out = self.out(torch.cat((up3, x),1))
        return out



def denoise_add_noise(x, t, pred_noise, z=None):
    if z is None:
        z = torch.randn_like(x)

    noise = b_t.sqrt()[t]*z
    mean = (x-pred_noise*((1-a_t[t])/(1-ab_t[t]).sqrt()))/a_t
    return mean + noise

nn_model = ContextUnet(in_channels=3, n_feat=n_feat, n_cfeat=n_cfeat, height=height)

## training ##
optim = torch.optim.Adam(nn_model.parameters(), lr=lrate)

def perturb_input(x, t, noise):
    return ab_t.sqrt()[t, None, None, None]*x + (1-ab_t[t, None, None, None])*noise

nn_model.train()

for ep in range(n_epoch):
    print(f"epoch {ep}")
    optim.param_groups[0]['lr'] = lrate*(1-ep/n_epoch)

    pbar = tqdm(dataloader, mininterval=2)
    for x, _ in pbar:
        optim.zero_grad()
        x = x.to(device)

        ## noisy image
        noise = torch.randn_like(x)
        t = torch.randint(1, timesteps+1, (x.shape[0],)).to(device)
        x_pert = perturb_input(x, t, noise)

        pred_noise = nn_model(x_pert, t/timesteps)

        loss = F.mse_loss(pred_noise, noise)
        loss.backward()
        optim.step()

    if ep%4==0 or ep==int(n_epoch-1):
        torch.save(nn_model.state_dict(), f"model_{ep}.pth")



## 生成图片
#nn_model
@torch.no_grad()
def sample_ddpm(n_sample, save_rate=20):
    samples = torch.randn(n_sample, 3., height, height).to(device)
    intermediate = []
    for i in range(timesteps, 0, -1):
        t = torch.tensor((i/timesteps))[:, None, None, None].to(device)
        ## 如果不加z , 生成图片质量差
        z = torch.randn(samples) if i > 0 else 0 
        eps = nn_model(samples, t)
        samples = denoise_add_noise(samples, i, eps, z)
        if i % save_rate == 0 or t == timesteps or i <0:
            intermediate.append(samples.detach().cpu().data)

    intermediate = np.stack(intermediate)
    return samples, intermediate



