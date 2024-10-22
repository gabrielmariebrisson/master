from starter_autoencoders import Autoencoder, LinearAutoEncoder
import torch
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Generate a dataset
n_samples = 1000
n_features = 10
encoding_dim = 2
data = np.random.randn(n_samples, n_features)

# Standardize the data
scaler = StandardScaler()
data = scaler.fit_transform(data)

# Convert data to PyTorch tensor for autoencoder
x = torch.FloatTensor(data)

# Train linear autoencoder
autoencoder = LinearAutoEncoder(n_features, encoding_dim)
autoencoder.train(x, n_epochs=200, lr=0.01)

# Get encoded representation from autoencoder
encoded_data = autoencoder.encode(x).detach().numpy()

# Train PCA
pca = PCA(n_components=encoding_dim)
pca_data = pca.fit_transform(data)

# Compare reconstruction errors
# Autoencoder reconstruction
reconstructed_data_ae = autoencoder.decode(autoencoder.encode(x)).detach().numpy()
reconstruction_error_ae = np.mean((data - reconstructed_data_ae)**2)
print(f'Reconstruction error for autoencoder: {reconstruction_error_ae}')

# PCA reconstruction
reconstructed_data_pca = pca.inverse_transform(pca_data)
reconstruction_error_pca = np.mean((data - reconstructed_data_pca)**2)
print(f'Reconstruction error for PCA: {reconstruction_error_pca}')

# Calculate explained variance ratio for PCA
explained_variance_ratio = pca.explained_variance_ratio_
print(f'Explained variance ratio (PCA): {explained_variance_ratio}')
print(f'Total variance explained (PCA): {np.sum(explained_variance_ratio):.4f}')

# Visualize the results
plt.figure(figsize=(12, 5))

# Plot encoded representations
plt.subplot(121)
plt.scatter(encoded_data[:, 0], encoded_data[:, 1], alpha=0.5, label='Autoencoder')
plt.scatter(pca_data[:, 0], pca_data[:, 1], alpha=0.5, label='PCA')
plt.title('Encoded Representations')
plt.legend()

# Plot reconstruction errors
plt.subplot(122)
bars = plt.bar(['Autoencoder', 'PCA'], 
               [reconstruction_error_ae, reconstruction_error_pca])
plt.title('Reconstruction Errors')
plt.ylabel('Mean Squared Error')

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.4f}',
             ha='center', va='bottom')

plt.tight_layout()
plt.show()