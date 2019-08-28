import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('3.jpg')

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


############################################################
############################################################
######################### IMAGE 1 ##########################
############################################################
############################################################

##### Image Binary #####
ret , img_binary = cv2.threshold(img,100,255,cv2.THRESH_BINARY)

##### Image Threshold binary inverse #####

ret , img_binary_inv = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)

##### Image Threshold Trunc ########

ret , img_trunc = cv2.threshold(img,150,255,cv2.THRESH_TRUNC)

##### Image Threshold TOZERO Inverse ########

ret , img_to_zero = cv2.threshold(img,150,255,cv2.THRESH_TOZERO)

############################################################
############################################################
######################### IMAGE 2 ##########################
############################################################
############################################################

img = cv2.imread('4.jpg',0)

ret , src1 = cv2.threshold(img,180,255,cv2.THRESH_BINARY)

src2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)

final_result = cv2.addWeighted(src1=src1,alpha=.4,src2=src2,beta=.6,gamma=10)

plt.imshow(final_result,cmap='gray')
plt.show()

