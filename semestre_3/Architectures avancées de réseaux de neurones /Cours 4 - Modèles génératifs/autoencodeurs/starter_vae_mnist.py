# In this file, we will use the vae to compress the MNIST dataset.
# We will also test the quality of the reconstruction by computing the reconstruction erro and visualizing the results.
# We will then use the compressed data to train a classifier.

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

from starter_VAE import VAE

# Load the MNIST dataset
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

transform = transforms.Compose([transforms.ToTensor(), transforms.Lambda(lambda x: x.view(-1))])
train_dataset = datasets.MNIST('data', train=True, download=True, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)


#x = torch.tensor(train_dataset.data[:1000].float().view(-1, 28*28), dtype=torch.float32).detach()
x = train_dataset.data[:1000].float().view(-1, 28*28).clone().detach()

# Train vaes
# TODO: use a very simple vae with only one hidden layer, and a small encoding dimension

input_dim = 28 * 28  # Dimension de l'entrée (images de 28x28 pixels)
encoding_dim = 32  # Petite dimension de l'encodage
# layers = [(input_dim, 128, 'relu'),
#         (128, 128, 'relu'),
#         (128, encoding_dim, 'relu'), ]  # Une seule couche cachée
layers =  [(input_dim, 512, 'relu'), 
        (512, 256, 'relu'), 
        (256, encoding_dim, 'relu')]


# Create and train vae
print("Creating vae with architecture:")
print(f"Input dimension: {input_dim}")
print(f"Encoding dimension: {encoding_dim}")
print(f"Hidden layers: {layers}")

vae = VAE(input_dim, encoding_dim, layers)
print("\nTraining vae...")
vae.train(train_loader, n_epochs=15, lr=0.001)

# Compute and display reconstruction error
with torch.no_grad():
    recon_x, mu, log_var = vae(x)
    reconstruction_error = vae.loss_function(recon_x, x, mu, log_var)
    print(f'\nReconstruction error: {reconstruction_error:.6f}')

# Compute the reconstruction error
reconstruction_error = F.mse_loss(recon_x, x).item()
print(f'Reconstruction error for vae: {reconstruction_error}')

# Visualize an example of the reconstruction
fig, axs = plt.subplots(2, 10, figsize=(20, 4))
for i in range(10):
    ax = axs[0, i]
    ax.imshow(x[i].view(28, 28).numpy(), cmap='gray')
    ax.set_title('Original')
    ax.axis('off')

    ax = axs[1, i]
    ax.imshow(recon_x[i].view(28, 28).numpy(), cmap='gray')
    ax.set_title('Reconstructed')
    ax.axis('off')

plt.show()

