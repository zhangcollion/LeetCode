import torch


def get_attention(x, adj):
    n, m = x.shape
    row_data = x.repeat(1,n)
    x_row = row_data.reshape(-1, m)
    x_col = x.repeat(n, 1)
<<<<<<< HEAD
    x_data = torch.cat((x_row, x_col), dim=1)
    x_dataT = x_data.T
    param_att = nn.Parameter(torch.FloatTensor(1, x_dataT.shape[1]))
    att_data = torch.matmul(param_att, x_dataT)
=======
    ## reshape to [n,n,2m]
    x_data = torch.cat((x_row, x_col), dim=1).view(n, -1, 2*m)
    param_att = nn.Parameter(torch.FloatTensor(x_dataT.shape[1],1))
    att_data = torch.matmul(x_dataT, param_att)
>>>>>>> EGNNA
    act = nn.LeakyReLU()
    att = torch.exp(act(att_data))
    x = torch.matmul(att, x)
    return att, x


