
from lightning import LightningModule
import torch
import torch.nn as nn 
import torch.optim as optim

from data import Caltech101DataLoader
from model import BasicConvNet
import torchvision.transforms as transforms
from sklearn.metrics import accuracy_score
import torchmetrics

class PLModel(LightningModule):
    """Implement a LightningModule that wrap a PyTorch module.

    TODO - Step 3.2: Implement the PyTorch Lightning wrapper to a PyTorch model.
        -  Implement the `training_step` method that does:
            - the forward pass
            - the loss computation
            - return the loss
            - compute metrics such as accuracy
        - Implement the `configure_optimizers` method that configure and return the optimiser (SGD, Adam, etc.)
    """
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.criterion = nn.CrossEntropyLoss()
        num_classes =1000
        self.train_accuracy = torchmetrics.Accuracy(task="multiclass", num_classes=num_classes)
        self.val_accuracy = torchmetrics.Accuracy(task="multiclass", num_classes=num_classes)


    def training_step(self, batch, batch_idx):
        # TODO: Split the batch into input and output data, then move them to the correct device
        inp, out = batch
        inp, out = inp.to(self.device), out.to(self.device)
        # TODO: Perform forward pass
        pred = self(inp)
        # TODO: Compute loss function between predictions and ground truth
        loss = self.criterion(pred, out)
        # TODO: Compute metrics
        #   - See `torchmetrics` classes for some implementation
        #   - Remember to log the metric and set prog_bar to True
        #   Refer to https://lightning.ai/docs/torchmetrics/stable/pages/lightning.html#torchmetrics-in-pytorch-lightning for examples.
        self.train_accuracy(pred, out)
        acc = self.train_accuracy.compute()
        self.log('train_loss', loss, prog_bar=True)
        self.log('train_acc', acc, prog_bar=True)
        # TODO: return the loss
        return loss

    def validation_step(self, batch, batch_idx):
        # TODO: repeat the same steps as in `training_step`

        # TODO: Split the batch into input and output data, then move them to the correct device
        inp, out = batch
        inp, out = inp.to(self.device), out.to(self.device)
        # TODO: Perform forward pass
        pred = self(inp)
        # TODO: Compute loss function between predictions and ground truth
        loss = self.criterion(pred, out)
        # TODO: Compute metrics
        self.train_accuracy(pred, out)
        acc = self.train_accuracy.compute()
        self.log('train_loss', loss, prog_bar=True)
        self.log('train_acc', acc, prog_bar=True)
        # TODO: return the loss
        return loss

    def configure_optimizers(self):
        optimizer = optim.SGD(self.parameters())
        return optimizer
