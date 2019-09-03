import numpy as np
import cv2
import matplotlib.pyplot as plt

def display(img):

    plt.imshow(img,cmap='gray')
    plt.show()


def img():

    img = np.zeros((1000,1000))
    cv2.putText(img,text='ABCDEF', org= (10,500),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=8,color=(255,255,255),thickness=45)
    return img


img = img()


################## ERODE #####################

kernal = np.ones((10,10),dtype=np.uint8)

img_erode = cv2.erode(img,kernal,iterations=12)


################## Add OPEN MORPHOLOGY ###########

white_nis = np.random.randint(0,2,size=(1000,1000),dtype=np.uint8)

white_nis = white_nis * 255

result_noise = white_nis + img

img_morph = cv2.morphologyEx(result_noise,cv2.MORPH_OPEN,kernal)

############### Add Close MORPHOLOGY #############

white_nis = np.random.randint(0,2,size=(1000,1000),dtype=np.uint8)

white_nis = white_nis * -255

result_noise = white_nis + img

result_noise[result_noise==-255] =0

morph_clos = cv2.morphologyEx(result_noise,cv2.MORPH_CLOSE,kernal)


############### Gerdiant MORPHOLOGY ##############

white_nis = np.random.randint(0,2,size=(1000,1000),dtype=np.uint8)

white_nis = white_nis * -255

result_noise = white_nis + img

result_noise[result_noise==-255] =0

morph_clos = cv2.morphologyEx(result_noise,cv2.MORPH_CLOSE,kernal)
morph_clos = cv2.morphologyEx(morph_clos,cv2.MORPH_GRADIENT,kernal)

display(img_morph)