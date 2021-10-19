import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


import skimage.data as data
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color

img = Image.open('Image of micrograph1.JPG').convert('L')
npimg = np.asarray(img)
print(npimg)
percentage = []
for i in range(255):
    x, y = (npimg <i).nonzero()
    vals = npimg[x, y]
    percentage.append(vals.size/npimg.size)
    # print(vals.size/npimg.size)

plt.plot(np.linspace(1,255,num=255),percentage)
plt.xlabel('Monochrome pixel intensity')
plt.ylabel('Percentage of pixels with intensities below the pixel intensity on x')
plt.show()

# def image_show(image, nrows=1, ncols=1, cmap='gray'):
#     fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
#     ax.imshow(image, cmap='gray')
#     ax.axis('off')
#     return fig, ax
#
# image_show(npimg)