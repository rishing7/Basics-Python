import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('aish.JPG', 1)
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic' )
cv2.line(img, (0,0), (500,500), (0,255,0),15) #BGR

cv2.rectangle(img, (200,200),(500,500),(0,0,255),5)

cv2.circle(img,(100,100),55,(255,0,0),-1)##3rd arg-radius ,-1:for filled with mentioned color


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
