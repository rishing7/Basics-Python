import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('aish.JPG', 1)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic' )
plt.plot([0, 900],[900, 0], 'c', lineWidth = 3)
plt.show()
