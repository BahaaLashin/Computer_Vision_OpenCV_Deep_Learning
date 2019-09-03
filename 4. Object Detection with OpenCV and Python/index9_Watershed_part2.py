import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('5.jpg')

# Blur

img_blur = cv2.medianBlur(img,3)

# Gray

img_gray = cv2.cvtColor(img_blur,cv2.COLOR_BGR2GRAY)

# Threshold

ret ,img_threshold = cv2.threshold(img_gray,240,255,cv2.THRESH_BINARY_INV)

kernal = np.ones((10,10))

morph_open = cv2.morphologyEx(img_threshold,cv2.MORPH_OPEN,kernal)
bg = cv2.dilate(morph_open,kernal,iterations=1)
dist = cv2.distanceTransform(morph_open,cv2.DIST_L2,5)

ret , threshold2 = cv2.threshold(dist,0.5*dist.max(),255,cv2.THRESH_BINARY)

threshold2 = np.uint8(threshold2)

unknown = cv2.subtract(bg,threshold2)

plt.imshow(unknown,cmap='gray')
plt.show()
