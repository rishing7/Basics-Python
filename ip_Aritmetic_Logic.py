import numpy as np
import cv2
from matplotlib import pyplot as plt
img1 = cv2.imread('aish.JPG', 1)
img2 = cv2.imread('aish.JPG', 1)

add = img1 + img2

cv2.imshow('Added Image',add)
cv2.waitKey(0)
cv2.destroyAllWindows()
