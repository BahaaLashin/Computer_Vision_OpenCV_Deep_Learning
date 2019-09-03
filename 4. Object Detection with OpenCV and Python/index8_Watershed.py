import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('5.jpg')

# Blur

img_blur = cv2.medianBlur(img,3)

# Gray

img_gray = cv2.cvtColor(img_blur,cv2.COLOR_BGR2GRAY)

# Threshold

ret ,img_threshold = cv2.threshold(img_gray,200,255,cv2.THRESH_BINARY_INV)

# find contours

contours , hirerchy = cv2.findContours(img_threshold.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)


for i in range(len(contours)):

    if hirerchy[0][i][3] == -1:
        cv2.drawContours(img,contours,i,(255,0,0),8)

plt.imshow(img)
plt.show()

