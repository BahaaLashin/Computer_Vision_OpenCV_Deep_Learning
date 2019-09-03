import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('3.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

img_gray = np.float32(img_gray)

corners = cv2.goodFeaturesToTrack(img_gray,80,.01,10)

for i in corners:
    x,y = i.ravel()  # [[1,3]] to [1,3]

    cv2.circle(img,(x,y),5,(0,0,255),-1)

plt.imshow(img)
plt.show()
