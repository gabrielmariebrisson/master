
import torch
import torchvision


class UNet(torch.nn.Module):
    """
    This class will implement the UNet architecture as presented in the course.


    Rq: As in the previous TPs, there is no softmax layer.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conv64 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
            torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
            )

        self.conv128 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(128),
            torch.nn.ReLU(),
            torch.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(128),
            torch.nn.ReLU(),
            )
        
        self.conv256 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(256),
            torch.nn.ReLU(),
            torch.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(256),
            torch.nn.ReLU(),
            )
        
        self.conv512 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(512),
            torch.nn.ReLU(),
            torch.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(512),
            torch.nn.ReLU(),
            )

        self.conv1024 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=512, out_channels=1024, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(1024),
            torch.nn.ReLU(),
            torch.nn.Conv2d(in_channels=1024, out_channels=1024, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(1024),
            torch.nn.ReLU(),
            )
        
        self.maxPool1 = torch.nn.MaxPool2d(kernel_size=2, stride=2)
        self.maxPool2 = torch.nn.MaxPool2d(kernel_size=2, stride=2)
        self.maxPool3 = torch.nn.MaxPool2d(kernel_size=2, stride=2)
        self.maxPool4 = torch.nn.MaxPool2d(kernel_size=2, stride=2)

        self.convBack512 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=1024, out_channels=512, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(512),
            torch.nn.ReLU(),
            torch.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(512),
            torch.nn.ReLU(),
            )
        
        self.convBack256 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(256),
            torch.nn.ReLU(),
            torch.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(256),
            torch.nn.ReLU(),
            )

        self.convBack128 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(128),
            torch.nn.ReLU(),
            torch.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(128),
            torch.nn.ReLU(),
            )
        self.convBack64 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
            torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
            )
        self.convBack2 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=64, out_channels=2, kernel_size=1, stride=1, padding='same'),
            torch.nn.ReLU(),
            )
        
        self.upsample1 = torch.nn.Upsample(scale_factor=2, mode='nearest')
        self.upsample2 = torch.nn.Upsample(scale_factor=2, mode='nearest')
        self.upsample3 = torch.nn.Upsample(scale_factor=2, mode='nearest')
        self.upsample4 = torch.nn.Upsample(scale_factor=2, mode='nearest')


    def forward(self, x):
        x = self.conv64(x)
        X_64= torchvision.transforms.functional.crop(x,height = 392,width = 392)
        x = self.maxPool1(x)

        x = self.conv128(x)
        X_128= torchvision.transforms.functional.crop(x,height = 200,width = 200)
        x = self.maxPool2(x)

        x = self.conv256(x)
        X_256= torchvision.transforms.functional.crop(x,height = 104,width = 104)
        x = self.maxPool3(x)

        x = self.conv512(x)
        X_512= torchvision.transforms.functional.crop(x,height = 56,width = 56)
        x = self.maxPool4(x)

        x = self.conv1024(x)
        x = self.upsample1(x)

        x = self.convBack512(x + X_512)
        x = self.upsample2(x)

        x = self.convBack256(x + X_256)
        x = self.upsample3(x)

        x = self.convBack128(x + X_128)
        x = self.upsample3(x)

        x = self.convBack64(x + X_64)
        x = self.upsample4(x)

        x = self.convBack2(x)

        return x
