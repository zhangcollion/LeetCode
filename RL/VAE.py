import  argparse
import torch
import torch.utils.data
import torch.nn.functional as F
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torchvision.utils import save_image


parser = argparse.ArgumentParser(description='VAE MNIST Example')
parser.add_argument('--BATCH_SIZE', type=int, default=128, metavar='N',
                    help='input batch size for training (default: 128)')
parser.add_argument('--epochs', type=int, default=10, metavar='N',
                    help='number of epochs to train (default: 10)')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')
parser.add_argument('--log_interval', type=int, default=10, metavar='N',
                    help='how many batches to wait before logging training status')
args,know = parser.parse_known_args()

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
    KLD = -0.5 * torch.sum(1+logvar-mu.pow(2)-logvar.exp())
    return BCE+KLD



##  dataset-> dataloader
from torch.utils.data import  Dataset,DataLoader
import numpy as np
import pandas as pd
class MinstDataset(Dataset):
    def __init__(self,x, y=None):
        self.data = torch.from_numpy(x).float()
        if y is not None:
            y = y.astype(np.int)
            self.label = torch.LongTensor(y)
        else:
            self.label = None

    def __getitem__(self, item):
        if self.label is not None:
            return self.data[item], self.label[item]
        else:
            return self.data[item]

    def __len__(self):
        return len(self.data)

training_data = pd.read_csv('/kaggle/input/digit-recognizer/train.csv')
testing_data = pd.read_csv('/kaggle/input/digit-recognizer/test.csv')

train_y = training_data.iloc[:,[0]].values
train_x= training_data.iloc[:,1:].values/255
val_y = testing_data.iloc[:,[0]].values
val_x = testing_data.iloc[:,1:].values/255
train_set = MinstDataset(train_x, train_y)
val_set = MinstDataset(val_x, val_y)
train_loader = DataLoader(train_set, batch_size=args.BATCH_SIZE, shuffle=True) #only shuffle the training data
val_loader = DataLoader(val_set, batch_size=args.BATCH_SIZE, shuffle=False)


def train(epoch):
    model.train()
    train_loss = 0
    for batch_idx, (data, _) in enumerate(train_loader):
        data = data.to(device)
        optimizer.zero_grad()
        recon_batch, mu, logvar = model(data)
        loss = loss_function(recon_batch, data, mu, logvar)
        loss.backward()
        train_loss += loss.item()
        optimizer.step()
        if batch_idx % args.log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                       100. * batch_idx / len(train_loader),
                       loss.item() / len(data)))

        print('====> Epoch: {} Average loss: {:.4f}'.format(
            epoch, train_loss / len(train_loader.dataset)))

def test(epoch):
    model.eval()
    test_loss = 0
    with torch.no_grad():
        for i, (data, _) in enumerate(val_loader):
            data = data.to(device)
            recon_batch, mu, logvar = model(data)
            test_loss += loss_function(recon_batch, data, mu, logvar).item()
            if i == 0:
                n = min(data.size(0), 8)
                comparison = torch.cat([data[:n],
                                        recon_batch.view(args.BATCH_SIZE, 1, 28, 28)[:n]])

    test_loss /= len(val_loader.dataset)
    print('====> Test set loss: {:.4f}'.format(test_loss))


if __name__=="__main__":
    # for epoch in range(1, args.epochs + 1):
    #     train(epoch)
    #     test(epoch)
    #     with torch.no_grad():
    #         sample = torch.randn(64, 20).to(device)
    #         sample = model.decode(sample).cpu()
    #         save_image(sample.view(64, 1, 28, 28),
    #                    'results/sample_' + str(epoch) + '.png')

    import gzip

    f = gzip.open(r'E:\迅雷下载\train-images-idx3-ubyte.gz', 'r')

    image_size = 28
    num_images = 5

    import numpy as np

    f.read(16)
    buf = f.read(image_size * image_size * num_images)
    data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    data = data.reshape(num_images, image_size, image_size, 1)
