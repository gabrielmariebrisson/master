
import torch


class BasicConvNet(torch.nn.Module):
    """
    This class will implement the following ConvNet architecture (all Conv layers are followed by ReLU):
    - Conv2d with 7x7 kernel size, 32 filters, and stride 2
    - Conv2d with 3x3 kernel size, 32 filters, and stride 1
    - Conv2d with 3x3 kernel size, 64 filters, and stride 1
    - Max pooling with 2x2 kernel size, stride 2
    - Conv2d with 3x3 kernel size, 128 filters, and stride 1
    - Conv2d with 3x3 kernel size, 128 filters, and stride 1
    - Flatten
    - Linear layer without activation, as many filters as there are classes

    Rq: We don't add a softmax layer because the cross-entropy loss can be used without (in fact, it improves numerical stability when computing gradients)
    """
    def __init__(self, num_classes: int):
        super(BasicConvNet, self).__init__()
        
        # Define the layers of the ConvNet
        self.conv_layers = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=7, stride=2),  # Assuming input has 3 channels (RGB)
            torch.nn.ReLU(),
            torch.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, stride=1),
            torch.nn.ReLU(),
            torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2),
            torch.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1),
            torch.nn.ReLU(),
            torch.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, stride=1),
            torch.nn.ReLU(),
        )
        
        # Flatten layer
        self.flatten = torch.nn.Flatten()
        
        # Fully connected layer
        self.fc = torch.nn.Linear(in_features=128*48*48, out_features=num_classes)
        
    def forward(self, x):
        # Forward pass through the network
        x = self.conv_layers(x)  # Pass through convolutional layers
        #print(x.shape)
        x = self.flatten(x)      # Flatten the output
        x = self.fc(x)           # Pass through the fully connected layer
        return x