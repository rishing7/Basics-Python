import numpy as np
import cv2
#import matplotlib.pyplot as plt
#cv2.namedWindow("Image")
img = cv2.imread('D:/IMAGEPROCESSING/a.png',-1)
#IMREAD_COLOR 1
#IMREAD_UNCHANGED -1
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindow()
