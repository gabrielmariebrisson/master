""" TD1: Script d'entraînement d'un réseau de neurones convolutifs (CNN) pour de la classification des images
Objectifs:
- Prise en main de l'API de PyTorch
- Implémentation de la boucle d'entraînement et de validation from scratch
"""
import torch
import torch.nn as nn 
import torch.optim as optim

from data import Caltech101DataLoader
from model import BasicConvNet
from model_bis import VGG16
import torchvision.transforms as transforms
from sklearn.metrics import accuracy_score
import torchmetrics

# Hyper-parameters
n_epoch = 1
device = "mps" if torch.backends.mps.is_available() else "cpu"
#device = "cpu"
best_model_params_path = 'best_model_params.pt'

# TODO - Step 1: Define Pre-processing or input data and target labels:
#   - Using torchvision.transforms data augmentation classes, implement the following transformation on inputs:
#       - Data type conversion to float32

# Définir les transformations
input_transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Redimensionner toutes les images à 224x224
    transforms.Grayscale(num_output_channels=3),
    transforms.ToTensor(),
    transforms.ConvertImageDtype(torch.float32),
])
# Définir les transformations pour les cibles
target_transform = transforms.Compose([
    transforms.Lambda(lambda y: torch.tensor(y, dtype=torch.long)) 
])

# TODO - Step 2: Implement the data loader
#   - In "data.py" file, implement the Caltech101DataLoader class
#   - Use this class to retrieve both training and validation data loader
caltech_dataset = Caltech101DataLoader("./tmp/", input_transform, target_transform, download=True)  # Set download to True to download the dataset
train_loader = caltech_dataset.training_loader()
val_loader = caltech_dataset.validation_loader()


# TODO - Step 3: Implement the model
#   - In "model.py" file, implement the BasicConvNet class
model = BasicConvNet(101).to(device=device)
model = VGG16(101).to(device=device)

# TODO - Step 4: Training configuration
#   - Define the loss function (cf "CrossEntropyLoss" class)
#   - Define the optimiser (SGD with learning rate of 10e-2)
#   - Define the metrics (Accuracy)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
train_accuracy = torchmetrics.Accuracy(task="multiclass", num_classes=101).to(device)
val_accuracy = torchmetrics.Accuracy(task="multiclass", num_classes=101).to(device)


# TODO - Step 5: Implement the training loop and the validation loop
#   - Fill the missing TODOs in the following code
torch.save(model.state_dict(), best_model_params_path)
best_acc = 0.

for epoch in range(1, n_epoch + 1):
    print(f'Epoch {epoch:02d}/{n_epoch:02d}')
    print('-' * 10)

    # TODO - 5.1: Training loop
    #   - Implement each of the following steps
    model.train()
    train_ma_loss = 0.
    train_ma_acc = 0.
    best_val_acc = 0.
    print("Training starts...")
    for step, (inp, out) in enumerate(train_loader):
        # TODO: put data to the correct device
        inp = inp.to(device)
        out = out.to(device)

        # TODO: Reset gradients stored in the optimiser
        optimizer.zero_grad()

        # TODO: Perform forward pass
        pred =  model(inp)

        # TODO: Compute loss function between predictions and ground truth
        loss = criterion(pred, out)

        # TODO: Do backpropagation
        loss.backward()

        # TODO: Update optimiser internal parameters
        optimizer.step()

        train_ma_loss += loss.item()
        train_accuracy(pred, out)
        # TODO: Update moving average loss and accuracy
        print(f"\r{step+1:03d}/{len(train_loader):03d}: loss = {train_ma_loss/(step+1):.4f} - acc (train) = {train_accuracy.compute():.4f}", end="")
    print()  # new line

    val_loss = 0.
    val_acc = 0.
    print("Validation starts...")
    # TODO - 5.2: Validation loop
    for step, (inp, out) in enumerate(val_loader):
        # TODO: put data to the correct device
        inp = inp.to(device)
        out = out.to(device)

        # TODO: Perform forward pass
        pred =  model(inp)
        # TODO: Compute loss function between predictions and ground truth
        loss = criterion(pred, out)
        val_loss += loss.item()
        val_accuracy(pred, out)

        # TODO: Update moving average loss and accuracy
        print(f"\r{step+1:03d}/{len(train_loader):03d}: loss = {val_loss/(step+1):.4f} - acc (validation) = {val_accuracy.compute():.4f}", end="")
    print()  # new line

    if best_val_acc < val_acc:
        torch.save(model.state_dict(), best_model_params_path)
        print(f"Saving model with better perfs ({best_val_acc} -> {val_acc}")
        best_val_acc = val_accuracy.compute()
    train_accuracy.reset()
    val_accuracy.reset()

# TODO - Bonus steps:
#   - Improve data augmentation by adding random crop, random flip, etc.
#   - Try different ConvNet architectures
#   - Try other optimisers (Adam, RMSProp, ...) and learning rate
#   - Add learning rate scheduling (cf "torch.optim.lr_scheduler")
