
import torch
from torchvision import transforms
from torchvision.datasets import Caltech101
from torch.utils.data import DataLoader, Subset

# TODO - Step 2: implement the data loader class with the following methods
#   - The constructor must have a `root` parameter to locate the data and a bool `download` (False by default) to download the data.
#   - "training_loader": the data loader for the CalTech101 training dataset
#   - "validation_loader": the data loader for the CalTech101 validation dataset
#   Note: You can modify the method prototypes if needed.
class Caltech101DataLoader:
    def __init__(self, root: str, input_transform=None, target_transform=None, download: bool = False):
        self.root = root
        self.download = download
        self.data = Caltech101(root=self.root, download=self.download, transform=input_transform, target_transform=target_transform)

        # Calculer l'index de séparation pour l'ensemble d'entraînement et de validation
        self.train_size = int(len(self.data) * 0.8)
        self.val_size = len(self.data) - self.train_size

    def training_loader(self, batch_size=32, shuffle=True):
        # Créer un DataLoader pour l'ensemble d'entraînement
        train_subset = Subset(self.data, range(self.train_size))  # Sous-ensemble des 80%
        return DataLoader(train_subset, batch_size=batch_size, shuffle=shuffle)

    def validation_loader(self, batch_size=32, shuffle=False):
        # Créer un DataLoader pour l'ensemble de validation
        val_subset = Subset(self.data, range(self.train_size, len(self.data)))  # Sous-ensemble des 20%
        return DataLoader(val_subset, batch_size=batch_size, shuffle=shuffle)

"""
, and two data augmentation parameters `input_transform` and `target_transform`
#       that will be applied to image and labels respectively during training.   """