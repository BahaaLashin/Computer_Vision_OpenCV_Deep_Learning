import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('2.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

blur_img = cv2.blur(img,ksize=(6,6))

upper = max(0,.3* np.median(blur_img))

lower = min(255,1.7*np.median(blur_img))

edges = cv2.Canny(blur_img,threshold1=upper,threshold2=lower-120)

plt.imshow(edges)
plt.show()
