import torch
import torch.nn as nn
import torch.nn.functional as F 


def UnetModel(nn.Module):
    def __init__(self, out_channels, n_class): #out_channels=[64,128,256,512,1024]
        self.n_class = n_class
        self.double_conv = DoubleConv(1, out_channels[0])
        self.down_conv1 = DownConv(out_channels[0], out_channels[1])
        self.down_conv2 = DownConv(out_channels[1], out_channels[2])
        self.down_conv3 = DownConv(out_channels[2], out_channels[3])
        self.down_conv4 = DownConv(out_channels[3], out_channels[4])
        self.up_conv4 = UpConv(out_channels[4]，out_channels[3])
        self.up_conv3 = UpConv(out_channels[3]，out_channels[2])
        self.up_conv2 = UpConv(out_channels[2]，out_channels[1])
        self.up_conv1 = UpConv(out_channels[1]，out_channels[0])
        self.out_conv = nn.Conv2d(out_channels, n_class, kernel_size=(1, 1))


    def forward(self, x):
        x1 = self.double_conv(x)
        x2 = self.down_conv1(x1)
        x3 = self.down_conv2(x2)
        x4 = self.down_conv3(x3)
        x5 = self.down_conv4(x4)
        u4 = self.up_conv4(x5, x4)
        u3 = self.up_conv3(u4, x3)
        u2 = self.up_conv2(u3, x2)
        u1 = self.up_conv1(u2, x1)
        logits = self.out_conv(u1)
        return logits



class DownConv(nn.Module):
    def __init__(self, arg):
        super(DownConv, self).__init__()
        self.max_pool = nn.MaxPool2d(kernel_size=(2,2), stride=2)
        self.conv = DoubleConv(in_channels, out_channels)

    def forward(self, x):
        pool_x = self.max_pool(x)
        res_x = self.conv(x)
        return res_x
        

class UpConv(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(UpConv, self).__init__()
        self.upsample = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
        self.conv = DoubleConv(in_channels, out_channels)

    def forward(self, x1, x2):
        x1 = self.upsample(x1)
        n,c, h, w = x1.shape
        ## x2 crop to cat x1
        x2 = x2[:, :, 0：h, 0:w]
        x = torch.cat([x1, x2], dim=1)
        upconv_x = self.conv(x)
        return upconv_x


class DoubleConv(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size=(3,3)):
        super(DoubleConv, self).__init__
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size)
        self.bn = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size)
        self.act = nn.ReLU(inplace=True)
    

    def forward(self, x):
        x1 = self.conv1(x)
        x1 = self.bn(x1)
        x1 = self.act(x1)
        x2 = self.conv2(x1)
        x2 = self.bn(x2)
        x = self.act(x2)
        return x







