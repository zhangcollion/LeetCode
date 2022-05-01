import  argparse
import torch
import torch.utils.data
import torch.nn.functional as F
import torch.nn as nn
import torch.optim as optim
# from torchvision import datasets, transforms
# from torchvision.utils import save_image

class VAE(nn.Module):
    def __init__(self):
        super(VAE, self).__init__()
        self.fc1 = nn.Linear(784, 512)
        self.fc2 = nn.Linear(512, 20)
        self.fc3 = nn.Linear(512,20)
        self.fc4 = nn.Linear(20,512)
        self.fc5 = nn.Linear(512,784)

    def encode(self, x):
        h1 = F.relu(self.fc1(x))
        return self.fc2(h1), self.fc3(h1)

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5*logvar)
        eps = torch.randn_like(mu)
        return mu+eps*std

    def decode(self, z):
        h1 = F.relu(self.fc4(z))
        return torch.sigmoid(self.fc5(h1))

    def forward(self, x):
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        return self.decode(z), mu, logvar

device = "cuda" if torch.cuda.is_available()  else "cpu"
model = VAE().to(device)
optimizer = optim.Adam(model.parameters(), lr=1e-3)

def loss_function(reconx, x, mu, logvar):
    BCE = F.binary_cross_entropy(reconx, x.reshape(-1,784), reduction="sum")
    KLD =0.5 * torch.sum(1+logvar-mu.pow(2)-logvar.exp())
    return BCE+KLD