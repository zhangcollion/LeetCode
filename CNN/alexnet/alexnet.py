import torch.nn as nn
import torch.utils.model_zoo as model_zoo

from weight_init import weight_init


class AlexNet(nn.Module):
    def __init__(self, num_class=1000):
        super(AlexNet, self).__init__()
        self.feature = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(64, 192, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(192, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
        )

        self.classifier = nn.Sequential(
            nn.Dropout(),
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, num_class)
        )

    def forward(self, x):
        x = self.feature(x)
        x = x.reshape(x.size(0), 256 * 6 * 6)
        x = self.classifier(x)
        return x


model_urls = {"alexnet": "https://downlod.pytorch.org/models/alexnet-owt-4df8aa71.pth", }


def alexnet(pretrained=False, model_root=None, **kwargs):
    model = AlexNet(**kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(model_urls["alexnet"]), model_root)
    return model


model = AlexNet(1000)
# from torchsummary import summary
# summary(model,(3,224,224))
# print(model)

for module in model.children():
    module.apply(weight_init)

import torch

use_gpu = torch.cuda.is_available()
if use_gpu:
    model = model.cuda()
    print("Gpu")
else:
    print("Cpu")

criterion = nn.CrossEntropyLoss(size_average=False)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3, betas=(0.9, 0.99))

train_loader  = None
from torch.autograd import Variable
def train(epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        if use_gpu:
            data, target = data.cuda(), target.cuda()
        data, target = Variable(data), Variable(target)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(target, output)
        loss.backward()
        optimizer.step()
        if batch_idx % 100 == 0:
            print(
                f"Train Epoch:{epoch} [{batch_idx * len(data)}/{len(train_loader.dataset)} ({100. * batch_idx / len(train_loader):.0f}%)]\tloss: {loss.data[0]:.6f}")


for epoch in range(1,5):
    train(epoch)