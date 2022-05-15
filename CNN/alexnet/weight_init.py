import torch.nn as nn

def weight_init(layer):
    # print("layer---------", layer)
    if isinstance(layer, nn.Conv2d):
        import math
        n = layer.kernel_size[0]*layer.kernel_size[1]*layer.out_channels
        layer.weight.data.normal_(0, math.sqrt(2./n))
    elif isinstance(layer, nn.BatchNorm2d):
        layer.weight.data.fill_(1)
        layer.bias.data.zero_()


