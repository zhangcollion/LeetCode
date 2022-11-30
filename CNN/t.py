import torch
import numpy as np

a = np.array([[1,2,3],[3,4,5],[33,44,55]])
a = torch.from_numpy(a)
n, m  = a.shape
row = a.repeat(1, n)
x_row = row.reshape(-1, m)
x_col = a.repeat(n, 1)
x_data = torch.cat((x_row, x_col), dim=1)
print("asd"
torch.nn.LeakyReLU
print("asd")