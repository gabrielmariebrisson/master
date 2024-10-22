""" TD2: CNNs classiques pour la classification des images
Objectifs:
- Implémentation d'un réseau de neurones en suivant les indications d'un article scientifique
- Prise en main de PyTorch Lightning pour l'entraînement
"""
import torch

from data import Caltech101DataLoader
from model import VGG16
from plmodel import PLModel
import torchvision.transforms as transforms
from pytorch_lightning import Trainer
from pytorch_lightning.callbacks import ModelCheckpoint

# Hyper-parameters
n_epoch = 1
device = "cuda" if torch.cuda.is_available() else "cpu"
best_model_params_path = 'best_model_params.pt'

# TODO - Step 1: Define Pre-processing or input data and target labels:
#   - Using torchvision.transforms data augmentation classes, implement the following transformation on inputs:
#       - Data type conversion to float32

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
caltech_dataset = Caltech101DataLoader("../data")  # Change that path to one better fitting
train_loader = caltech_dataset.training_loader()
val_loader = caltech_dataset.validation_loader()

# TODO - Step 3: Implement the model
#   - In "model.py" file, implement the VGG16 and ResNet18 class
base_model = VGG16().to(device=device)

# TODO - Step 4: Training configuration
#   - Define the loss function (cf "CrossEntropyLoss" class)
#   - Define the metrics (Accuracy)
#   - In "plmodel.py" file, implement the lightning wrapper of the forward pass and the loss and metric computation, and the optimiser selection
model = PLModel(base_model)

# TODO - Step 5: Configure an experiment:
#   - Use the `lightning.Trainer` class to define the training procedure such that:
#       - A maximum number of epoch of `n_epoch`
#       - A progress bar for both training and validation
#       - Automatic model saving
#       - model validation after every epoch
#   See https://lightning.ai/docs/pytorch/stable/common/trainer.html#trainer-class-api for details.
# Checkpoint callback to save the best model
checkpoint_callback = ModelCheckpoint(
    monitor='val_acc',
    mode='max',
    save_top_k=1,
    dirpath='checkpoints/',
    filename='best_model'
)

# Trainer setup
trainer = Trainer(
    max_epochs=n_epoch,
    progress_bar_refresh_rate=20,
    gpus=1 if torch.cuda.is_available() else 0,
    callbacks=[checkpoint_callback],
    log_every_n_steps=50
)

# TODO - Step 6: Perform the training
#    - Use the `fit` method from the `lightning.Trainer` class
#    - Give both training and validation data loader
#
trainer.fit(model, train_dataloaders=train_loader, val_dataloaders=val_loader)


# TODO - Bonus steps:
#   - Add the implemented bonus from TP1
#   - Try other standard architecture, such as MobileNet or GoogleNet
#   Refs: Howard et al. "MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications", arXiv 2017
#         Szegedy et al. "Going Deeper with Convolutions",CVPR 2015.

