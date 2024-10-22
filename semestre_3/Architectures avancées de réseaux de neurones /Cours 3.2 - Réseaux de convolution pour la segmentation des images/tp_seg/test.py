from model import UNet

import torch
model = UNet()

image_rgb = torch.rand(3, 572, 572)

print("debut")
output = model(image_rgb)
print("fin")