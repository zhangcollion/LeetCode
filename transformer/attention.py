import torch
import torch.nn as nn
class Attention(nn.Module):
    def __init__(self, config, axial_name):
        super().__init__()
        self.num_heads = config.num_heads
        self.feat_dim = config.feat_dim
        self.ffn_dim = config.ffn_dim
        self.dp = config.get('dp', 0.1)
        self.axial_name = axial_name
        self.mask_threshold = -1e4
        self.d_k = self.feat_dim // self.num_heads
        self.query_transform =

