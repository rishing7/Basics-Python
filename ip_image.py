import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('aish.JPG', 1)
cv2.imshow('image',img)
px = img[55, 55]
#print(px)
img[100:150, 100:150] = [255,255,255]

aish_face=img[37:111, 107:194]
img[0:74, 0:87] = aish_face
cv2.imshow('image1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
