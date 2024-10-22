# Dataloaders for Deep Learning 
# -*- coding: utf-8 -*-

# Exercise 1: Batch Processing and Shuffle
# Task: Understand the impact of batch processing and shuffling on model training.

# Instructions:
# Create a Dataset and a DataLoader
# Use a simple dataset (e.g., Iris dataset) with PyTorch.
# Create a DataLoader with options for batch size and shuffling.
# Observe the Effects of Shuffling
# Train a classification model (e.g., a simple neural network) on data with and without shuffling.
# Compare the model performance (accuracy) using both configurations.

# Solution:
import torch
from torch.utils.data import DataLoader, TensorDataset
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

# Load a simple dataset
data = load_iris()
X = data.data
y = data.target

# Normalize the data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Convert to tensors
# to complete
# hint: torch.tensor
X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.long)

# Create a dataset
# to complete
# hint: TensorDataset
dataset = TensorDataset(X_tensor, y_tensor)

# Create two dataloaders: with and without shuffling
# to complete
# hint: DataLoader
batch_size = 16
loader_shuffle = DataLoader(dataset, batch_size=batch_size, shuffle=True)
loader_no_shuffle = DataLoader(dataset, batch_size=batch_size, shuffle=False)


# Function to train a simple model
def train_model(dataloader):
    # Define a simple model with 2 hidden layers
    model = torch.nn.Sequential(
        # to complete
        # hint: torch.nn.Linear, torch.nn.ReLU
        torch.nn.Linear(4, 16), 
        torch.nn.ReLU(),
        torch.nn.Linear(16, 16),
        torch.nn.ReLU(),
        torch.nn.Linear(16, 3)
    )   
    # Define a loss function and optimizer
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    
    # Train the model
    for epoch in range(10):  # Number of epochs
        for X_batch, y_batch in dataloader:
            optimizer.zero_grad()
            outputs = model(X_batch)
            loss = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()
    return model

# Train the models
# to complete
model_no_shuffle = train_model(loader_no_shuffle)
model_shuffle = train_model(loader_shuffle)

# Function to evaluate the model
# uncomment the following code
def evaluate_model(model):
    with torch.no_grad():
        outputs = model(X_tensor)
        _, predicted = torch.max(outputs, 1)
        accuracy = metrics.accuracy_score(y_tensor, predicted)
    return accuracy

# Evaluate the models
accuracy_no_shuffle = evaluate_model(model_no_shuffle)
accuracy_shuffle = evaluate_model(model_shuffle)

print(f'Accuracy without shuffling: {accuracy_no_shuffle}')
print(f'Accuracy with shuffling: {accuracy_shuffle}')


# Exercise 2: Data Augmentation
# Task: Apply data augmentation techniques and observe their impact on the model.

# Instructions:
# Load an Image Dataset: Use an image dataset (e.g., CIFAR-10 or MNIST) with PyTorch.
# Apply Data Augmentation: Use transformations such as rotations and flips on the dataset.
# Compare Performances:
# Train a classification model on both the original dataset and the augmented dataset.
# Compare the performance of the two models.

# Solution:
import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision import datasets, models

# Define transformations
transform_original = transforms.Compose([
    transforms.ToTensor(),
])

transform_augmented = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(30),
    transforms.ToTensor(),
])

# Load datasets
# trainset_original = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform_original)
# trainset_augmented = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform_augmented)
trainset_original = datasets.MNIST(root='./data', train=True, download=True, transform=transform_original)
trainset_augmented = datasets.MNIST(root='./data', train=True, download=True, transform=transform_augmented)


dataloader_original = DataLoader(trainset_original, batch_size=64, shuffle=True, num_workers=2)
dataloader_augmented = DataLoader(trainset_augmented, batch_size=64, shuffle=True, num_workers=2)

# Define a simple model

model = torch.nn.Sequential(
    torch.nn.Linear(28 * 28, 128),
    torch.nn.ReLU(),
    torch.nn.Linear(128, 10)
)

# Define a loss function and optimizer
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# Training function
def train_model(dataloader):
    for epoch in range(5):  # Number of epochs
        running_loss = 0.0
        for inputs, labels in dataloader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f'Epoch {epoch+1}, Loss: {running_loss/len(dataloader)}')

# Train the models
print("Training on original dataset...")
train_model(dataloader_original)
print("Training on augmented dataset...")
train_model(dataloader_augmented)

