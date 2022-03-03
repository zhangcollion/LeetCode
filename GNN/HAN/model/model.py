import torch
import torch.nn as nn
from ./layer import *

class HetaGAT_multi(nn.Module):
    def __init__(self, inputs_list, nb_classes, nb_nodes, 
                attn_drop, ffd_drop, bias_mat_list, hid_units, n_heads,
                activation=nn.ELU(), residual=False)
        super(HetaGAT_multi, self).__init__()
        self.inputs_list = inputs_list
        self.nb_classes = nb_classes
        self.nb_nodes = nb_nodes
        self.attn_drop = attn_drop
        self.ffd_drop = ffd_drop
        self.bias_mat_list = bias_mat_list
        self.hid_units = hid_units
        self.n_heads = n_heads
        self.activation = activation
        self.residual = residual
        self.mp_att_size = 128
        self.layer = self._make_attn_head()
        self.simpleAttLayer = SimpleAttLayer(64, self.mp_att_size, time_major=False, return_alphas=True)
        self.fc = nn.Linear(64, self.nb_classes)


    def _make_attn_head(self):
        layers = []
        for inputs, biases in zip(self.inputs_list, self.bias_mat_list):
            layers.append(Attn_head(in_channel=inputs.shape[1],out_sz=self.hid_units[0],bias_mat=biases,in_drop=self.ffd_drop,coef_drop=self.attn_drop,activation=self.activation,residual=self.residual))

        return nn.Sequential(*list(m for m in layers))

    def forward(self, x):
        embed_list = []
        for i, (inputs, biases) in enumerate(zip(x, self.bias_mat_list)):

            attns = []
            jhy_embeds = []
            for _ in range(self.n_head[0]):
                attns.append(self.layers[i](inputs))
            h_1 = torch.cat(attns, dim=1)\
            embed_list = append(torch.squeeze(h_1).reshape(h_1.shape[-1], 1, -1))
        multi_embed = torch.cat(embed_list, dim=1)
        final_embed, att_val = self.simpleAttLayer(multi_embed)
        out = []
        for i in range(self.n_head[-1]):
            out.append(self.fc(final_embed))

        return out[0]