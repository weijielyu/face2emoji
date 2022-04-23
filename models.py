import torch
import torch.nn
import torchvision.models as models

resnet18 = models.resnet18(pretrained=True)






class F2eResNet(nn.Module)