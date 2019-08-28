import numpy as np
import cv2
import matplotlib.pyplot as plt

def display(img):

    cv2.imshow('Frame',img)
    cv2.waitKey()


def img():

    img = cv2.imread('5.jpg').astype(np.float32)/255
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img


img = img()

############## Lighting ##################

gamma = 2

img_lighting = np.power(img,gamma)


############# Add Kernal #################

kernal = np.random.rand(10,10) - .45

img_filter = cv2.filter2D(img,-1,kernal)


############# Blur #######################

img_blur = cv2.blur(img,ksize=(20,20))


############# GaussianBlur ###############

img_Gu_Blur = cv2.GaussianBlur(img,(15,15),10)

############# mediam blue ##############

img_md_blur = cv2.medianBlur(img,5)

plt.imshow(img_md_blur)
plt.show()