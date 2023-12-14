import torch
from unet import UNet
import cv2
import matplotlib.pyplot as plt
from torchvision import transforms
import sys

image = cv2.imread(sys.argv[1])
image = cv2.resize(image, (572, 572))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
transform = transforms.ToTensor()
image = transform(image)
shape = image.shape
print(shape)
image = image.reshape(1, shape[0], shape[1], shape[2])
print(image.shape)

model = UNet(2)
model_dict = torch.load('models/UNet5.pt')
model.load_state_dict(model_dict['model_state_dict'])

import time
t = time.time()
prediction = model(image)
print(time.time() - t)

image = image[0][0].detach().numpy()
prediction = prediction[0][0].detach().numpy()

cv2.imwrite(sys.argv[2], prediction)

fig, axs = plt.subplots(1, 2)
axs[0].imshow(image, cmap='gray')
axs[1].imshow(prediction, cmap='gray')
plt.savefig('visualization/UNet50_2.png')
plt.show()