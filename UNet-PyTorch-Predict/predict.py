import torch
from unet import UNet
import matplotlib.pyplot as plt
from torchvision import transforms
import sys
import os
from PIL import Image

image = Image.open(sys.argv[1])
image = image.resize((572, 572))

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

# cv2.imwrite(sys.argv[2], prediction)
plt.tight_layout()
plt.axis('off')
plt.imshow(prediction, cmap='gray')
plt.savefig(sys.argv[2], pad_inches=0, bbox_inches='tight')
plt.close()

if not os.path.exists('visualization'):
    os.mkdir('visualization')

fig, axs = plt.subplots(1, 2)
axs[0].imshow(image, cmap='gray')
axs[1].imshow(prediction, cmap='gray')
axs[0].axis('off')
axs[1].axis('off')
plt.tight_layout()
plt.savefig('visualization/UNet5_2.png')