# A PyTorch class for autoencoders

import torch
import torch.nn as nn
import torch.nn.functional as F

class Autoencoder(nn.Module):
    # Constructor: 
    #   - input_dim is the dimension of the input data, 
    #   - encoding_dim is the dimension of the encoding layer, 
    #   - layers is a list of dims together with the activation functions for the hidden layers. The list is of the form [(dim1, dim2, activation), ...]
    #     where activation is either 'relu', 'sigmoid' or linear
    def __init__(self, input_dim, encoding_dim, layers=[]):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential()
        self.decoder = nn.Sequential()
        
        for i, layer in enumerate(layers):
            self.encoder.add_module(f'Linear{i}', nn.Linear(layer[0], layer[1]))
            if layer[2] == 'relu':
                self.encoder.add_module(f'Relu{i}', nn.ReLU())
            elif layer[2] == 'sigmoid':
                self.encoder.add_module(f'Sigmoid{i}', nn.Sigmoid())
            else:
                self.encoder.add_module(f'Identity{i}', nn.Identity())

        for i, layer in enumerate(layers[::-1]):
            self.decoder.add_module(f'Linear{i}', nn.Linear(layer[1], layer[0]))
            if layer[2] == 'relu':
                self.decoder.add_module(f'Relu{i}', nn.ReLU())
            elif layer[2] == 'sigmoid':
                self.decoder.add_module(f'Sigmoid{i}', nn.Sigmoid())
            else:
                self.decoder.add_module(f'Identity{i}', nn.Identity())

    def forward(self, x):
        x = self.decode(self.encode(x))
        return x
    
    def train(self, x, n_epochs=100, lr=0.01):
        optimizer = torch.optim.Adam(self.parameters(), lr=lr)
        criterion = nn.MSELoss()
        for epoch in range(n_epochs):
            optimizer.zero_grad()
            output = self(x)
            loss = criterion(output, x)
            loss.backward()
            optimizer.step()
            if epoch % 10 == 0:
                print(f'Epoch {epoch}: loss = {loss.item()}')
    
    def encode(self, x):
        return self.encoder(x)
    
    def decode(self, x):
        return self.decoder(x)
    
class LinearAutoEncoder(Autoencoder):
    def __init__(self, input_dim, encoding_dim):
        super(LinearAutoEncoder, self).__init__(input_dim, encoding_dim)
        
        # For a linear autoencoder, we only need two linear layers:
        # One for encoding (input_dim -> encoding_dim)
        # One for decoding (encoding_dim -> input_dim)
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, encoding_dim)
        )
        
        self.decoder = nn.Sequential(
            nn.Linear(encoding_dim, input_dim)
        )
        
        # Initialize the weights using Xavier initialization
        for module in self.modules():
            if isinstance(module, nn.Linear):
                nn.init.xavier_uniform_(module.weight)
                if module.bias is not None:
                    nn.init.zeros_(module.bias)

if __name__ == '__main__':
    # Fix the example in main to match the correct parameters
    ae = Autoencoder(4, 2, layers=[(4, 3, 'relu'), (3, 2, 'linear')])
    # Test the LinearAutoEncoder
    linear_ae = LinearAutoEncoder(4, 2)
    # Create some random data
    x = torch.randn(100, 4)
    # Train the autoencoder
    linear_ae.train(x, n_epochs=100)