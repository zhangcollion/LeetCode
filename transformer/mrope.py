import torch
import torch.nn as nn


class EnhancedMultimodalRoPE3D(nn.Module):
    def __init__(self, dim=1024, base=10000, max_pos=10000):
        super().__init__()
        self.dim = dim
        self.base = base
        self.max_pos = max_pos

        # 针对 dim=1024 的硬编码切分: [340, 342, 342] (均为偶数)
        self.dim_parts = [340, 342, 342]
        assert sum(self.dim_parts) == dim, f"Dim parts {sum(self.dim_parts)} != {dim}"

        # 预计算并注册三个维度的频率缓冲区
        for i, d_part in enumerate(self.dim_parts):
            inv_freq = 1.0 / (base ** (torch.arange(0, d_part, 2).float() / d_part)) ## f**(-2i/d)
            self.register_buffer(f"inv_freq_{i}", inv_freq)

    def forward(self, x, positions):
        """
        Apply M-RoPE to input features.

        Args:
            x: Tensor of shape [B, num_heads, L, dim]
            positions: Tensor of shape [B, L, 3] -> (modal_id, height, width)

        Returns:
            x_out: Tensor of shape [B, num_heads, L, dim]
        """
        B, H, L, D = x.shape
        assert D == self.dim, f"Input dim {D} != expected {self.dim}"
        assert positions.shape == (B, L, 3), f"Position shape {positions.shape} invalid"

        # Step 1: Split x into 3 segments along feature dim
        x_split = torch.split(x, self.dim_parts, dim=-1)  # List of 3 tensors

        # Step 2: Unbind positions into modal, h, w
        pos0, pos1, pos2 = positions.unbind(dim=-1)  # Each: [B, L]
        pos_list = [pos0, pos1, pos2]

        results = []
        for i in range(3):
            x_part = x_split[i]  # [B, H, L, d_i]
            pos = pos_list[i]  # [B, L]
            inv_freq = getattr(self, f"inv_freq_{i}")  # [d_i // 2]

            # Normalize position
            pos_norm = pos / self.max_pos  # [B, L]

            # Compute frequencies: [B, L, d_i//2]
            # 广播式外积：将每个位置值与所有频率基底相乘
            freqs = torch.einsum('bl,d->bld', pos_norm, inv_freq) # [B, L] ==>  [B, L, d_i//2]

            # Expand to full dimension: [B, L, d_i]
            emb = torch.cat([freqs, freqs], dim=-1)  # [B, L, d_i]

            # Reshape for batched rotation: [B*H, L, d_i]
            x_flat = x_part.reshape(B * H, L, -1)
            cos_val = emb.unsqueeze(1).expand(-1, H, -1, -1).reshape(B * H, L, -1).cos()
            sin_val = emb.unsqueeze(1).expand(-1, H, -1, -1).reshape(B * H, L, -1).sin()

            # Apply RoPE: split and rotate
            x1, x2 = x_flat.chunk(2, dim=-1)  # [B*H, L, d_i//2] each
            x_rot = torch.cat([-x2, x1], dim=-1)  # [B*H, L, d_i]

            # Rotate
            x_rotated = x_flat * cos_val + x_rot * sin_val  # [B*H, L, d_i] ## x0与x(d/2),x1与x(d/2+1)配对

            # Reshape back
            x_rotated = x_rotated.view(B, H, L, -1)  # [B, H, L, d_i]
            results.append(x_rotated)

        # Concatenate all parts
        return torch.cat(results, dim=-1)


# ==================== 调试与测试脚本 ====================
if __name__ == "__main__":
    # 设置随机种子以便复现
    torch.manual_seed(42)

    # 初始化 M-RoPE 模块
    mrope = EnhancedMultimodalRoPE3D(dim=1024, base=10000, max_pos=1000)

    # 构造模拟输入
    B, num_heads, L = 2, 8, 50
    x = torch.randn(B, num_heads, L, 1024)  # [B, H, L, 1024]

    # 构造位置编码: [B, L, 3]
    # 假设:
    #   modal_id: 0=image, 1=text, 2=bev
    #   height, width: 在 0~500 范围内
    positions = torch.zeros(B, L, 3)
    positions[:, :, 0] = torch.randint(0, 3, (B, L)).float()  # modal_id
    positions[:, :, 1] = torch.rand(B, L) * 500  # height
    positions[:, :, 2] = torch.rand(B, L) * 500  # width

    print("Input x shape:", x.shape)
    print("Positions shape:", positions.shape)

    # 前向传播
    with torch.no_grad():
        output = mrope(x, positions)

    print("Output shape:", output.shape)
    print("Output stats: mean={:.4f}, std={:.4f}".format(output.mean().item(), output.std().item()))

    # 验证输出是否合理（无 NaN/Inf）
    assert not torch.isnan(output).any(), "Output contains NaN!"
    assert not torch.isinf(output).any(), "Output contains Inf!"

    print("✅ Test passed! M-RoPE works correctly.")

    # query = self.with_pos_embed(src_feat, query_pos)
    # key = self.with_pos_embed(dst_feat, key_pos)
    # def  with_pos_embed(self, tensor, pos=None):
    #     return tensor if pos is None else tensor + pos