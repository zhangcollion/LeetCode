import torch
import numpy as np
import random
from torch.utils.data import DataLoader
from torch import optim
import torch
from seed_pkg.random_data import random_data
from seed_pkg.model_def import *

def seed_setting(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
# seed_setting(3407)


if __name__ == "__main__":
    seed_setting(3407)
    print(torch.initial_seed())
    print(0, "\n", np.random.randn(3, 3))
    random_data()

    user_dataset = UserDataset()
    user_loader = DataLoader(user_dataset, batch_size=32, shuffle=True)


    model = reg_model(1, 1)
    criterior = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.1)
    for i in range(2):
        for x, y in user_loader:
            optimizer.zero_grad()
            pred_y = model(x)
            loss = criterior(pred_y, y)
            loss.backward()
            optimizer.step()
        for param_tensor in model.state_dict():  # 字典的遍历默认是遍历 key，所以param_tensor实际上是键值
            print(param_tensor, '\t', model.state_dict()[param_tensor])
        print("------------------loss------------------", loss.detach().numpy())

    print("------------------model done------------------")