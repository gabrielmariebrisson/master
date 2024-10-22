# Comparing Keras, PyTorch, and PyTorch Lightning Implementations using MNIST Dataset
# -*- coding: utf-8 -*-
# Task: llustrate the differences between Keras, PyTorch, and PyTorch Lightning by 
# implementing a simple neural network to classify the MNIST dataset. 
# This exercise demonstrates the structure, ease of use, and flexibility of each framework.

# Instructions:

# 1. Implement a neural network using each framework (Keras, PyTorch, PyTorch Lightning) to train on the MNIST dataset.
# 2. Compare the code structure, readability, and flexibility between the three implementations.
# 3. Measure and compare training time and performance.

# 1. Keras Implementation
# Solution:
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist

print("Keras Implementation")
# Load the MNIST dataset
# to complte
# hint: use the load_data() function from mnist
# hint: normalize the data

# Define a simple neural network model
model = Sequential([
    # to complete
    # hint: Flatten and Dense layers
])
# Another way to define the model
# to complete

# Compile the model
# to complete
# hint: specify the optimizer, loss function, and metrics

# Train the model
# to complete
# hint: use the fit() function

# Evaluate the model
# to complete
# hint: use the evaluate() function

# print(f"Keras Model Accuracy: {accuracy:.4f}")

# Key Points:

# Ease of Use: Minimal boilerplate code; the Sequential API makes defining layers straightforward.
# Training Process: Simple model.fit() handles training, validation, and logging.
# Use Case: Best suited for beginners or projects requiring rapid prototyping.

# 2. PyTorch Implementation
# Solution:
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

print("\nPyTorch Implementation")
# Define transformations for the dataset
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

# Load the MNIST dataset
train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
test_dataset = datasets.MNIST(root='./data', train=False, transform=transform, download=True)
train_loader = DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=64, shuffle=False)

# Define a simple neural network model
class SimpleNN(nn.Module):
    def __init__(self):
        # to complete
        # hint: define the layers (Flatten, Linear, ReLU, Linear, Softmax)

    def forward(self, x):
        # to complete
        # hint: define the forward pass

# Initialize the model, loss function, and optimizer
# uncomment the following lines
# model = SimpleNN()
# criterion = nn.CrossEntropyLoss()
# optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
# def train(model, device, train_loader, optimizer, criterion):
#     model.train()
#     for epoch in range(5):
#         for batch_idx, (data, target) in enumerate(train_loader):
#             data, target = data.to(device), target.to(device)
#             optimizer.zero_grad()
#             output = model(data)
#             loss = criterion(output, target)
#             loss.backward()
#             optimizer.step()
#         print(f"Epoch {epoch + 1}: Loss = {loss.item():.4f}")

# Evaluation function
# def test(model, device, test_loader):
#     model.eval()
#     correct = 0
#     with torch.no_grad():
#         for data, target in test_loader:
#             data, target = data.to(device), target.to(device)
#             output = model(data)
#             pred = output.argmax(dim=1, keepdim=True)
#             correct += pred.eq(target.view_as(pred)).sum().item()
#     accuracy = correct / len(test_loader.dataset)
#     print(f"PyTorch Model Accuracy: {accuracy:.4f}")

# Move model to device (CPU or GPU) and run training and evaluation
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# model.to(device)
# train(model, device, train_loader, optimizer, criterion)
# test(model, device, test_loader)

# Key Points:

# Flexibility: Full control over the training loop, which can be customized for research purposes.
# Training Process: Manually handles forward pass, loss computation, backpropagation, and optimizer step.
# Use Case: Preferred for research projects where model behavior needs to be tweaked frequently.


# 3. PyTorch Lightning Implementation
# Solution:
import pytorch_lightning as pl
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchmetrics.classification import Accuracy

# Define the PyTorch Lightning model
class LightningMNISTClassifier(pl.LightningModule):
    def __init__(self):
        super(LightningMNISTClassifier, self).__init__()
        self.model = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, 10),
            nn.LogSoftmax(dim=1)
        )
        self.criterion = nn.CrossEntropyLoss()
        self.accuracy = Accuracy(task='multiclass', num_classes=10)  # Specify task type and number of classes
        self.val_accuracies = []  # To store validation accuracies for printing

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = self.criterion(y_hat, y)
        self.log('train_loss', loss, on_step=True, on_epoch=True, prog_bar=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = self.criterion(y_hat, y)
        acc = self.accuracy(y_hat.argmax(dim=1), y)  # Compute accuracy
        self.log('val_loss', loss, prog_bar=True)
        self.log('val_accuracy', acc, prog_bar=True)  # Log the accuracy
        self.val_accuracies.append(acc)  # Save accuracy for epoch end
        return loss

    def on_validation_epoch_end(self):
        # Calculate average accuracy across all batches and print
        avg_acc = torch.stack(self.val_accuracies).mean()
        print(f'Validation Accuracy: {avg_acc:.4f}')
        self.val_accuracies.clear()  # Clear the accuracies list for the next epoch

    def configure_optimizers(self):
        return optim.Adam(self.parameters(), lr=0.001)

# Data preparation
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
mnist_train = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
mnist_test = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
train_loader = DataLoader(mnist_train, batch_size=64, shuffle=True)
val_loader = DataLoader(mnist_test, batch_size=64, shuffle=False)

# Initialize the model and PyTorch Lightning Trainer
model = LightningMNISTClassifier()
trainer = pl.Trainer(max_epochs=5, accelerator='gpu' if torch.cuda.is_available() else 'cpu')
trainer.fit(model, train_loader, val_loader)

# Exercise Summary and Comparison:
# Keras: Simplifies model creation and training with minimal code, great for quick experimentation.
# PyTorch: Offers maximum control and customization, suited for research and custom model adjustments.
# PyTorch Lightning: Streamlines PyTorch code, reducing boilerplate and adding scalability, perfect for research moving towards production.


