""" TD3: Modèles classiques pré-entraîné pour la classification des images
Objectifs:
- Utiliser PyTorch et PyTorch Lightning pour le transfert learning + fine-tuning d'architectures de réseaux de neurones
"""

# TODO - Step 1: Don't start from scratch
#   - Start from TD2 project

# TODO - Step 2: Update the base model
#   - Replace re-implemented models by one of the `torchvision.models`
#   - Load both the architecture and pre-trained weights
#   - Remove the last fully connected layer and add one for Caltech101
#   - Re-train et evaluate the new model


# TODO - bonus steps:
#   - modify the learning rate to have two different learning rates:
#       - a smaller one for the pre-trained architecture
#       - a higher one for the newly added layer
#   - Try and compare different pre-trained architectures
