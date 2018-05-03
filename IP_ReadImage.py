import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('aish.JPG', 1)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic' )
plt.xticks([]),plt.yticks([])
#cv2.waitkey(0)
#cv2.destroyAllWindows()
plt.show()
