import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg')

##### Convert To RGB ###

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

##### Convert to HLS ####

img_hls = cv2.cvtColor(img,cv2.COLOR_RGB2HLS)

##### Convert To HSV ####

img_hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

plt.imshow(img_hsv)
plt.show()