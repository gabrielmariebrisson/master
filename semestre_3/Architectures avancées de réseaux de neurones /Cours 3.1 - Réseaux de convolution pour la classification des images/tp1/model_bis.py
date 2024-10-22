
import torch


class VGG16(torch.nn.Module):
    """
    This class will implement the VGG 16 architecture according to
    Simonyan and Zisserman, "Very Deep Convolutional Networks for Large-Scale Image Recognition", ICLR 2015.

    The correct architecture to implement is available in Table 1, configuration D. Note that the last layer named "FC-1000"
    stands for fully connected with 1000 neurones which corresponds to the 1000 classes of ImageNet. You have to modify this layer
    to fit any class number.

    Note: Again, we don't add a softmax activation.
    """
    def __init__(self, num_classes: int):
        super(VGG16, self).__init__()

        # Define the layers of the ConvNet
        self.conv64 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding='same'),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
            torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding='same'),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
        )
        self.conv128 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding='same'),
            torch.nn.BatchNorm2d(128),
            torch.nn.ReLU(),
            torch.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, stride=1, padding='same'),
            torch.nn.BatchNorm2d(128),
            torch.nn.ReLU(),
        )
        self.conv256Init = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, stride=1, padding='same'),
            torch.nn.BatchNorm2d(256),
            torch.nn.ReLU(),
        )
        self.conv256 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, stride=1, padding='same'),
            torch.nn.BatchNorm2d(256),
            torch.nn.ReLU(),
        )
        self.conv512Init = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, stride=1, padding='same'),
            torch.nn.BatchNorm2d(512),
            torch.nn.ReLU(),
        )
        self.conv512 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, stride=1, padding='same'),
            torch.nn.BatchNorm2d(512),
            torch.nn.ReLU(),
        )
        self.maxPool1= torch.nn.MaxPool2d(kernel_size=2, stride=2)
        self.maxPool2= torch.nn.MaxPool2d(kernel_size=2, stride=2)
        self.maxPool3= torch.nn.MaxPool2d(kernel_size=2, stride=2)
        self.maxPool4= torch.nn.MaxPool2d(kernel_size=2, stride=2)
        self.maxPool5= torch.nn.MaxPool2d(kernel_size=2, stride=2)
        self.gap = torch.nn.AdaptiveAvgPool2d(1)
        
        # Fully connected layer
        self.fc1 = torch.nn.Linear(in_features=512, out_features=4096)
        self.fc2 = torch.nn.Linear(in_features=4096, out_features=4096)
        self.fc3 = torch.nn.Linear(in_features=4096, out_features=num_classes)

    def forward(self, x):
        x = self.conv64(x)
        x = self.maxPool1(x)

        x = self.conv128(x)
        x = self.maxPool2(x)

        x = self.conv256Init(x)
        x = self.conv256(x)
        x = self.conv256(x)
        x = self.maxPool3(x)

        x = self.conv512Init(x)
        x = self.conv512(x)
        x = self.conv512(x)
        x = self.maxPool4(x)

        x = self.conv512(x)
        x = self.conv512(x)
        x = self.conv512(x)
        x = self.maxPool5(x)

        x = self.gap(x)
        x = x.view(x.size(0), -1)

        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x

        

         


class ResNet18(torch.nn.Module):
    """
    This class will implement the ResNet 18 architecture according to
    He et al., "Deep Residual Learning for Image Recognition", CVPR 2016.

    The correct architecture to implement is available in Table 1, configuration with 18 layers. Each block corresponds to the architecture presented in Figure 5.

    To ease the implementation, you can define an intermediate method (or another class) that build each block.

    Similar to VGG16, the last layer named "FC-1000" is for classification with ImageNet, and should be replaced to fit any class number.

    Note: Again, we don't add a softmax activation.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        raise NotImplementedError(f"{self.__class__.__name__} is not implemented.")

    def forward(self, x):
        raise NotImplementedError("'forward' method not implemented.")
