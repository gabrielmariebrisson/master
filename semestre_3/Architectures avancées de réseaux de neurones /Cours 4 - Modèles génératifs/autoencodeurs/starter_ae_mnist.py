# In this file, we will use the autoencoder to compress the MNIST dataset.
# We will also test the quality of the reconstruction by computing the reconstruction erro and visualizing the results.
# We will then use the compressed data to train a classifier.

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

from starter_autoencoders import Autoencoder

# Load the MNIST dataset
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

transform = transforms.Compose([transforms.ToTensor(), transforms.Lambda(lambda x: x.view(-1))])
train_dataset = datasets.MNIST('data', train=True, download=True, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)


x = torch.tensor(train_dataset.data[:1000].float().view(-1, 28*28), dtype=torch.float32)

# Train autoencoders
# TODO: use a very simple autoencoder with only one hidden layer, and a small encoding dimension

input_dim = 28 * 28  # Dimension de l'entrée (images de 28x28 pixels)
encoding_dim = 16  # Petite dimension de l'encodage
# layers = [(input_dim, 128, 'relu'),
#         (128, 128, 'relu'),
#         (128, encoding_dim, 'relu'), ]  # Une seule couche cachée
layers =  [(input_dim, 512, 'relu'), 
            (512, 256, 'relu'), 
            (256, 128, 'relu'), 
            (128, 64, 'relu'), 
            (64, encoding_dim, 'relu')]


# Create and train autoencoder
print("Creating autoencoder with architecture:")
print(f"Input dimension: {input_dim}")
print(f"Encoding dimension: {encoding_dim}")
print(f"Hidden layers: {layers}")

autoencoder = Autoencoder(input_dim, encoding_dim, layers)
print("\nTraining autoencoder...")
autoencoder.train(x, n_epochs=5000, lr=0.001)

# Compute and display reconstruction error
with torch.no_grad():
    reconstructed_data = autoencoder.decode(autoencoder.encode(x))
    reconstruction_error = F.mse_loss(x, reconstructed_data).item()
    print(f'\nReconstruction error: {reconstruction_error:.6f}')


# 

# Compute the reconstruction error
reconstructed_data = autoencoder.decode(autoencoder.encode(x)).detach().numpy()
reconstruction_error = np.mean((x.numpy() - reconstructed_data)**2)
print(f'Reconstruction error for autoencoder: {reconstruction_error}')

# Visualize an example of the reconstruction
import matplotlib.pyplot as plt
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(x[1].view(28, 28).numpy(), cmap='gray')
plt.title('Original image')
plt.subplot(1, 2, 2)
plt.imshow(reconstructed_data[1].reshape(28, 28), cmap='gray')
plt.title('Reconstructed image')
plt.show()

# TODO: Try with different architectures and hyperparameters to see how the reconstruction error evolves


