""" TD4: Importance des convolutions en images: comparaison CNN / NN
Objectifs:
- Vérifier expérimentalement la capacité des CNNs à être invariant par translation
"""

# TODO - Step 1: Don't start from scratch
#   - Start from TD2 project

# TODO - Step 2: Change dataset for faster analysis
#   - Replace Caltech101 by MNIST

# TODO - Step 3: Build 2 similar (and small) models
#   - CNNs with Conv2d + global Pooling + linear
#   - NN with as much linear layers as conv layers + flatten + linear

# TODO - Step 4: Training and evaluation
#   - Design 2 data augmentation setups:
#       - 1 that do zero-padding with 12 pixels to each side (MNIST images are now of size 28+2*12 = 52 pixels)
#       - 1 that randomly translate the number (28x28 pixels) in a 52x52 black image
#   - Train and validate on MNIST both networks with the first data augmentation
#   - Test on MNIST both networks with the second data augmentation, and analyse obtained results
#       - You have to implement the `test_step` in PyTorch Lightning

# TODO - bonus steps:
#   - evaluate the impact of strides, local pooling, etc. on the translation invariance property
