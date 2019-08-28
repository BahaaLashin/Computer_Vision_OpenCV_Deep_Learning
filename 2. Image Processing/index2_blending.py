import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('1.jpg')

img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

img2 = cv2.imread('2.png')
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

############# ADD WEIGHTED ###########
img1 = cv2.resize(img1,(500,500))
img2 = cv2.resize(img2,(500,500))
blening_img = cv2.addWeighted(src1=img1,alpha=.8,src2=img2,beta=.2,gamma=10)

############# Blending as a logo ########

img1 = cv2.imread('1.jpg')

img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

img2 = cv2.imread('2.png')
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

larg_img = img1
larg_img = cv2.cvtColor(larg_img,cv2.COLOR_RGB2GRAY)
small_img = img2
small_img = cv2.cvtColor(small_img,cv2.COLOR_RGB2GRAY)

arr = small_img >20


logo = larg_img[0:small_img.shape[1],0:small_img.shape[0]]

logo2 =  np.where(small_img < 200, small_img, 255)



plt.imshow(larg_img,cmap='gray')
plt.show()