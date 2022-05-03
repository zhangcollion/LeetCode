from torch.autograd import Function

class ReverseLayerF(Function):

    @staticmethod
    def forward(ctx, x, alpha):
        ctx.alpha = alpha
        return x.view_as(x)

    # backward()的输入只有2个(ctx, grad_output)
    # ctx必须有，grad_output是最终object对的forward()输出的导数
    @staticmethod
    def backward(ctx, grad_output):
        output = grad_output.neg() * ctx.alpha
        return output, None


## network
import torch.nn as nn
class CNNmodel(nn.Module):
    def __init__(self):
        super(CNNmodel, self).__init__()
        self.feature = nn.Sequential()
        self.class_feature = nn.Sequential()
        self.domain_feature = nn.Sequential()

    def forward(self, input_data, alpha):
        input_data = input_data.expand(input_data.data.shapep[0],3,28,28)
        feature = self.feature(input_data)
        feature = feature.view(-1, 50*4*4)
        reverse_feature = ReverseLayerF.apply(feature,alpha)
        class_output = self.class_feature(feature)
        domain_output = self.domain_feature(reverse_feature)

        return class_output, domain_output

my_net = CNNmodel()
# setup optimizer
import torch
import torch.optim as optim

optimizer = optim.Adam(my_net.parameters(), lr=1e-3)

my_net.zero_grad()
class_output, domain_output = my_net(input_data=input_img, alpha=alpha)
err_s_label =  torch.nn.NLLLoss(class_output, class_label)
err_s_domain =  torch.nn.NLLLoss(domain_output, domain_label)