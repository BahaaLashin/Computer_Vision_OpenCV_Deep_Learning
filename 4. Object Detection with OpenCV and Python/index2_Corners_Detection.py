import cv2
import matplotlib.pyplot as plt
import numpy as np

################## part 1 ##################
img = cv2.imread('3.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

img_gray = np.float32(img_gray)

dist = cv2.cornerHarris(img_gray,blockSize=2,ksize=5,k=.04)
dist = cv2.dilate(dist,None)

img[dist> 0.01*dist.max()] = [255,255,255]

################## part 2 ##################

img = cv2.imread('2.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

img_gray = np.float32(img_gray)

dist = cv2.cornerHarris(img_gray,blockSize=3,ksize=5,k=.04)
dist = cv2.dilate(dist,None)

img[dist> 0.01*dist.max()] = [255,255,255]


plt.imshow(img)
plt.show()

