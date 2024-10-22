# GPU vs CPU
# -*- coding: utf-8 -*-

# Fisrt sactivate the virtual environment with the following command:
# source /net/ens/DeepLearning/python3/tensorflow2/bin/activate
# Exercise 1: Matrix Multiplication
# Implement the matrix multiplication function using the CPU and GPU.
# Task:
# Implement and compare the performance of matrix multiplication on both CPU and GPU using PyTorch.
# Instructions:
# Create two large random matrices (e.g., size 3000 x 3000).
# Perform matrix multiplication using CPU.
# Perform the same multiplication using GPU (CUDA).
# Measure and compare the execution times.

# Solution:
import torch
import time


# Check if cuda is available or not. If cuda is not available, try mps, if mps is not available, exit.
# hint: torch.cuda.is_available() 
if torch.cuda.is_available():
    device = torch.device('cuda')
    print("CUDA is available. Using GPU.")
elif torch.backends.mps.is_available():
    device = torch.device('mps')
    print("MPS is available. Using Apple Silicon GPU.")
else:
    print("Neither CUDA nor MPS is available. Exiting.")
    exit()

# Set matrix size
matrix_size = 3000

# Generate two random matrices A and B
# hint: torch.randn()
A = torch.randn(matrix_size, matrix_size)
B = torch.randn(matrix_size, matrix_size)

# Exercise on CPU
# Perform matrix multiplication on CPU
# hint: torch.matmul() and time.time()
start_cpu = time.time()
result_cpu = torch.matmul(A, B)
end_cpu = time.time()
cpu_time = end_cpu - start_cpu
print(f"Matrix multiplication on CPU took {cpu_time:.6f} seconds.")


# Move matrices to GPU
# hint: to(device)
A = A.to(device)
B = B.to(device)


# Exercise on GPU (or mps)
# Perform matrix multiplication on GPU
# hint: torch.matmul() and time.time()
start_gpu = time.time()
result_gpu = torch.matmul(A, B)
torch.cuda.synchronize() if torch.cuda.is_available() else None  # Ensure synchronization for CUDA
end_gpu = time.time()
gpu_time = end_gpu - start_gpu
print(f"Matrix multiplication on {device} took {gpu_time:.6f} seconds.")

# Output the results
print(f"Matrix multiplication time on CPU: {cpu_time:.4f} seconds")
print(f"Matrix multiplication time on {device}: {gpu_time:.4f} seconds")
print(f"Speedup: {cpu_time / gpu_time:.2f}x")

# Warning: be carreful to move both matrices to the same device (CPU or GPU) before performing the multiplication.


# Exercise 2: Neural Network Training (CPU vs. GPU)
# Task:
# Train a simple neural network on the MNIST dataset using CPU and GPU, and compare the training times.
# Instructions:
# Define a simple neural network (e.g., 2-layer fully connected).
# Load the MNIST dataset 
# Train the network using CPU, measure the time taken for one epoch.
# Train the same network using GPU, and measure the time taken for one epoch.
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import time

# Define a simple neural network
class SimpleNN(nn.Module):
    def __init__(self):
        # to complete
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)
        self.fc2 = nn.Linear(128, 10)  

    def forward(self, x):
        # to complete
        x = x.view(-1, 28*28)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Load MNIST dataset
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

# Initialize the model, loss function, and optimizer
model = SimpleNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training on CPU
device_cpu = torch.device('cpu')
model.to(device_cpu)
start_time_cpu = time.time()
for images, labels in train_loader:
    images, labels = images.to(device_cpu), labels.to(device_cpu) 
    optimizer.zero_grad()
    outputs = model(images)
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()
end_time_cpu = time.time()
cpu_training_time = end_time_cpu - start_time_cpu

# Training on GPU
if torch.cuda.is_available():
    device = torch.device('cuda')
    print("CUDA is available. Using GPU.")
elif torch.backends.mps.is_available():
    device = torch.device('mps')
    print("MPS is available. Using Apple Silicon GPU.")
else:
    print("Neither CUDA nor MPS is available. Exiting.")
    exit()
# Move model to GPU
model.to(device) 

# set the device to cuda and move the model to the device (be careful to move the model to the device before the loop)

start_time_gpu = time.time()
for images, labels in train_loader:
    # to complete
    # move the images and labels to the device
    images, labels = images.to(device), labels.to(device)

    optimizer.zero_grad()
    outputs = model(images)
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()
end_time_gpu = time.time()
gpu_training_time = end_time_gpu - start_time_gpu

# Output the results
print(f"Training time on CPU: {cpu_training_time:.4f} seconds")
print(f"Training time on {device}: {gpu_training_time:.4f} seconds")
print(f"Speedup: {cpu_training_time / gpu_training_time:.2f}x")
