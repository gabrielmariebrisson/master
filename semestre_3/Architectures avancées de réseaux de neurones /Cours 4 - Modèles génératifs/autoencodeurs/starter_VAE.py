import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# VAE class
class VAE(nn.Module):
    def __init__(self, input_dim: int, encoding_dim: int, layers: list):
        super(VAE, self).__init__()
        self.encoder = nn.Sequential()
        self.decoder = nn.Sequential()
        # Encoder
        for i, layer in enumerate(layers):
            self.encoder.add_module(f'Linear{i}', nn.Linear(layer[0], layer[1]))
            if layer[2] == 'relu':
                self.encoder.add_module(f'Relu{i}', nn.ReLU())
            elif layer[2] == 'sigmoid':
                self.encoder.add_module(f'Sigmoid{i}', nn.Sigmoid())
            else:
                self.encoder.add_module(f'Identity{i}', nn.Identity())
        
        # Latent space
        self.fc_mu = nn.Linear(layers[-1][1], encoding_dim)
        self.fc_var = nn.Linear(layers[-1][1], encoding_dim)
        
        # Decoder
        for i, layer in enumerate(layers[::-1]):
            self.decoder.add_module(f'Linear{i}', nn.Linear(layer[1], layer[0]))
            if layer[2] == 'relu':
                self.decoder.add_module(f'Relu{i}', nn.ReLU())
            elif layer[2] == 'sigmoid':
                self.decoder.add_module(f'Sigmoid{i}', nn.Sigmoid())
            else:
                self.decoder.add_module(f'Identity{i}', nn.Identity())

    def encode(self, x: torch.Tensor):
        h = self.encoder(x)
        mu = self.fc_mu(h)
        log_var = self.fc_var(h)
        return mu, log_var

    def reparameterize(self, mu: torch.Tensor, log_var: torch.Tensor):
        std = torch.exp(0.5 * log_var)
        eps = torch.randn_like(std)
        return mu + eps * std

    def decode(self, z: torch.Tensor):
        x = self.decoder(z)
        return x

    def forward(self, x: torch.Tensor):
        mu, log_var = self.encode(x)
        z = self.reparameterize(mu, log_var)
        return self.decode(z), mu, log_var

    def loss_function(self, recon_x: torch.Tensor, x: torch.Tensor, mu: torch.Tensor, log_var: torch.Tensor):
        recon_loss = F.mse_loss(recon_x, x, reduction='sum')
        kl_loss = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())
        return recon_loss + kl_loss

    def train(self, dataloader, n_epochs=100, lr=0.001, lr_patience=10, lr_factor=0.1):
        optimizer = torch.optim.Adam(self.parameters(), lr=lr)
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=lr_patience, factor=lr_factor)
        best_loss = float('inf')
        patience = 0

        for epoch in range(n_epochs):
            total_loss = 0
            for batch_idx, (data, _) in enumerate(dataloader):
                optimizer.zero_grad()
                recon_x, mu, log_var = self.forward(data)
                loss = self.loss_function(recon_x, data, mu, log_var)
                loss.backward()
                optimizer.step()
                total_loss += loss.item()

            avg_loss = total_loss / len(dataloader)
            scheduler.step(avg_loss)

            if avg_loss < best_loss:
                best_loss = avg_loss
                patience = 0
            else:
                patience += 1

            if patience >= 10:
                print(f"Early stopping triggered after {epoch} epochs.")
                break

            print(f'Epoch {epoch}: loss = {avg_loss}')



# Example of usage
if __name__ == '__main__':
    from torch.utils.data import DataLoader, TensorDataset
    
    # Generate random data
    data = torch.randn(28 * 28, 28 * 28)
    dataset = TensorDataset(data, data)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
    
    # Create VAE model
    input_dim = 28 * 28
    encoding_dim = 32

    layers =  [(input_dim, 512, 'relu'), 
            (512, 256, 'relu'), 
            (256, encoding_dim, 'relu')]
    vae = VAE(input_dim, encoding_dim, layers)
    
    # Train the model
    vae.train(dataloader)
