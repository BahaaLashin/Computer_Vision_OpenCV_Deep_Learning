import numpy as np
import cv2
import matplotlib.pyplot as plt

def display(img):

    plt.imshow(img,cmap='gray')
    plt.show()


img = cv2.imread('6.jpg',0)

kernal = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])

################# Sobel X ##########

sobelX = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)

################ Sobel Y ###########

sobelY = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

################ Leplacian ##########

laplacian = cv2.Laplacian(img,6)

################## Gredient ##########
blending = cv2.addWeighted(src1=sobelX,alpha =.5,src2 = sobelY , beta=.5 ,gamma=100000000)


ret , th = cv2.threshold(img,100,255,cv2.THRESH_BINARY)

kernal = np.ones((3,3),dtype=np.uint8)

gredient = cv2.morphologyEx(th,cv2.MORPH_GRADIENT,kernal)

img = cv2.imread('3.jpg')


display(gredient)
