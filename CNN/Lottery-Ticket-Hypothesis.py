## 定义big_model  性能可训练到比较好
#涉及
    # 1、初始化
def weight_init(m):
    import torch.nn.init as init
    if isinstance(m, nn.Conv2d):
        init.normal_(m.weight.data)
        if m.bias is not None:
            init.normal_(m.bias)
    elif isinstance(m, ConvTranspose2d):
        init.normal_(n.weight.data)
        if m.bias is not None:
            init.normal_(m.bias.data)
    elif isinstance(m, nn.GRU):
        for param in m.parameters():
            if len(param.shape) >= 2:
                init.orthogonal_(param.data)
            else:
                init.normal_(param.data)
    # 2、根据big_model 定义mask_matrix
def make_mask(model):
    global step
    global make_mask
    step = 0
    for name, param in model.named_parameters():
        if 'weight' in name:
            step = step + 1

    #每层weight对应一个mask矩阵
    mask = [None] * step
    step = 0 
    for name, param in model.named_parameters():
        if 'weight' in name:
            param_data = param.data.cpu().numpy()
            mask[step] = np.ones_like(param_data)
            step += 1
    step = 0

# 大模型剪枝 按percent 比例剪枝
def prune_by_percentile(percent, resample=False, reinit=False,**kwargs):
    global step
    global mask
    global model
    step = 0
    for name, param in model.named_parameters():
        if 'weight' in name:
            param_data = param.data.cpu().numpy()
            alive = param_data[np.nonzero(param_data)] # flattened array of nonzero values
            percentile_value = np.percentile(abs(alive), percent)

            weight_dev = param.device
            new_mask = np.where(abs(tensor) < percentile_value, 0, mask[step])

            param.data = torch.from_numpy(tensor * new_mask).to(weight_dev)
            mask[step] = new_mask
            step += 1

            

    step = 0


## 模型训练
def train(model, train_loader, optimizer, criterion):
    EPS = 1e-6
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.train()
    for batch_idx, (imgs, targets) in enumerate(train_loader):
        optimizer.zero_grad()
        #imgs, targets = next(train_loader)
        imgs, targets = imgs.to(device), targets.to(device)
        output = model(imgs)
        train_loss = criterion(output, targets)
        train_loss.backward()

        # Freezing Pruned weights by making their gradients Zero [Pruned weights本身也为0]
        for name, p in model.named_parameters():
            if 'weight' in name:
                tensor = p.data.cpu().numpy()
                grad_tensor = p.grad.data.cpu().numpy()
                grad_tensor = np.where(tensor < EPS, 0, grad_tensor)
                p.grad.data = torch.from_numpy(grad_tensor).to(device)

        optimizer.step()

    return train_loss.item()




