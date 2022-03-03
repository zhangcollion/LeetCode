import torch
import torch.nn as nn

class Atten_head(nn.Module):

    def __init__(self, in_channel, out_sz, bias_mat, in_drop=0.0, coef_drop=0.0
                activation=None, residual=False, return_coef=False):
        super(Atten_head, self).__init__()
        self.bias_mat = bias_mat
        self.in_drop = in_drop
        self.coef_drop = coef_drop
        self.return_coef = return_coef
        self.conv1 = nn.Conv1d(in_channel, out_sz, 1, bias=False)
        self.conv2_1 = nn.Conv1d(out_sz, 1, 1, bias=False)
        self.conv2_2 = nn.Conv1d(out_sz, 1, 1, bias=False)
        self.leakyrelu = nn.LeakyReLU()
        self.softmax = nn.Softmax()
        self.in_dropout = nn.Dropout(in_drop)
        self.coef_drop = nn.Dropout(coef_drop)
        self.activation = activation

    def forward(self, x):
        seq = x.float()
        if self.in_drop != 0.0:
            seq = self.in_dropout(x)
            seq = seq.float()
        seq_fts = self.conv1(seq)
        f_1 = self.conv2_1(seq_fts)
        f_2 = self.conv2_2(seq_fts)
        logits = f_1 + torch.transpose(f_2, 2, 1)
        logits = self.leakyrelu(logits)
        coefs = self.softmax(logits+self.bias_mat.float())
        if self.coef_drop != 0.0:
            coefs = self.coef_drop(coefs)
        if self.in_drop != 0.0:
            seq_fts = self.in_dropout(seq_fts)

        ret = torch.matmul(coefs, torch.transpose(seq_fts, 2, 1))
        ret = torch.transpose(ret, 2, 1)
        if self.return_coef:
            return self.activation(ret), coefs
        else:
            return self.activation(ret)


class SimpleAttLayer(nn.Module):
    def __init__(self, inputs, attention_size, time_major=False, return_alpha=False):
        super(SimpleAttLayer, self).__init__()
        self.hidden_size = inputs
        self.return_alpha = return_alpha
        self.time_major = time_major
        self.w_omega = nn.Parameter(torch.Tensor(self.hidden_size, attention_size))
        self.b_omega = nn.Parameter(torch.Tensor(attention_size))
        self.u_omege = nn.Parameter(torch.Tensor(attention_size, 1))
        self.tanh = nn.Tanh()
        self.softmax = nn.Softmax()
        self.reset_parameters()

    def reset_parameters(self):
        nn.init.xavier_uniform_(self.w_omega)
        nn.init.zeros(self.b_omega)
        nn.init.xavier_uniform_(self.u_omege)

    def forward(self, x):
        v = self.tanh(torch.matmul(x, self.w_omega)+self.b_omega)
        vu = torch.matmul(v, self.u_omege)
        alphas = self.softmax(xu)
        output = torch.sum(x*alphas,reshape(alphas.shape[0], -1, -1), dim=1)
        if not self.return_alphas:
            return output
        else:
            return output, alphas









