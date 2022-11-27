import torch
import torch.nn as nn
import torch.nn.functional as F

"""
resnet Implementation
"""

class BasicBlock(nn.Module):
    def __init__(self, in_channel, out_channel, stride=1, kernel_size=3):
        super(BasicBlock, self).__init__()
        self.in_channel = in_channel
        self.out_channel = out_channel
        self.kernel_size = kernel_size
        self.conv1 = nn.Conv2d(in_channel, self.out_channel ,self.kernel_size,stride, padding=1)
        self.bn1 = nn.BatchNorm2d()
        self.conv2 = nn.Conv2d(self.out_channel, self.out_channel, self.kernel_size, stride, padding=1)
        self.bn2 = nn.BatchNorm2d()
        self.act = nn.ReLU()


    def forward(self, x):
        res_x = x
        x1 = self.conv1(x)
        norm_x1 = self.bn1(x1)
        act_norm_x1 = self.act(norm_x1)
        x2 = self.conv2(act_norm_x1)
        norm_x2 = self.bn2(x2)
        result_x = norm_x2 + res_x
        result_x = self.act(result_x)
        return result_x


class ResNet(nn.Module):
    def __init__(self, in_channel, blocks, filters, stride, num_class):
        resnet = nn.ModelList()
        self.conv1 = nn.Conv2d(in_channel, 64, kernel_size=7, stride=2)
        block_channel = 64
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2) 
        self.bn = nn.BatchNorm2d()
        self.relu = nn.ReLU()
        for block_num, filter_num in zip(blocks, filters):
            for i in range(block_num):
                res_block = BasicBlock(block_channel,filter_num)
                resnet.append(res_block)
            block_channel = filter_num
        self.avgpool = nn.AdaptiveAvgPool1d((1,1))
        self.fc = nn.Linear(512*4, num_class)      
        self.act = nn.Softmax()

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn(x)
        x = self.relu(x)
        x = self.maxpool(x)
        for conv_layer in resnet:
            x = conv_layer(x)
        x = self.avgpool(x)
        x = torch.flatten(x)
        x = self.fc(x)
        x = self.act(x)
        return x



