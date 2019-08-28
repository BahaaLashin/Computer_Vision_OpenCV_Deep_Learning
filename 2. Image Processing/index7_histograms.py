import numpy as np
import cv2
import matplotlib.pyplot as plt

def display(img):

    plt.imshow(img,cmap='gray')
    plt.show()


img = cv2.imread('1.jpg')


hist0 = cv2.calcHist([img],channels=[0],mask=None,histSize=[256],ranges=[0,256])
hist1 = cv2.calcHist([img],channels=[1],mask=None,histSize=[256],ranges=[0,256])
hist2 = cv2.calcHist([img],channels=[2],mask=None,histSize=[256],ranges=[0,256])

plt.plot(hist0,color='blue')
plt.plot(hist1,color='green')
plt.plot(hist2,color='red')
plt.show()