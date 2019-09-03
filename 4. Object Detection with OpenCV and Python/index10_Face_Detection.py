import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('8.jpg',0)

cascade = cv2.CascadeClassifier('faceFront.xml')

def multi_cascade(img):

    img_copy=  img.copy()

    res_cascade = cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=5)

    for (x,y,w,h) in res_cascade:

        cv2.rectangle(img_copy,(x,y),(x+w,y+h),(255,255,255),8)

    return img_copy



plt.imshow(multi_cascade(img),cmap='gray')
plt.show()

