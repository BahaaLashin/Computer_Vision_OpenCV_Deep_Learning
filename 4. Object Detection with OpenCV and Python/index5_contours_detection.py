import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('4.webp',0)

contours , hierarchy  = cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

external_contours = np.zeros(img.shape)

for i in range(len(contours)):

    if hierarchy[0][i][3] == -1:
        cv2.drawContours(external_contours,contours,i,255,-1)

internal_contours = np.zeros(img.shape)

for i in range(len(contours)):

    if hierarchy[0][i][3] != -1:
        cv2.drawContours(internal_contours,contours,i,255,-1)

plt.imshow(external_contours)
plt.show()


