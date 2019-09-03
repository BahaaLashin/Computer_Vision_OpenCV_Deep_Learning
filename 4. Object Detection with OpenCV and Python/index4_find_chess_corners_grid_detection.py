import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('3.jpg')

img_blur = cv2.blur(img,(5,5))

img_gray = cv2.cvtColor(img_blur,cv2.COLOR_BGR2GRAY)

ret , img_threshold = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)

found ,corners = cv2.findChessboardCorners(img_threshold,(7,7))

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.drawChessboardCorners(img,(7,7),corners,found)

plt.imshow(img)
plt.show()
