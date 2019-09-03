import cv2
import matplotlib.pyplot as plt
import numpy as np

full = cv2.imread('1.jpg')
full = cv2.cvtColor(full,cv2.COLOR_BGR2RGB)
face = cv2.imread('1.face.jpg')
face = cv2.cvtColor(face,cv2.COLOR_BGR2RGB)

methods = ['cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED','cv2.TM_CCORR','cv2.TM_CCORR_NORMED','cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED']

for m in methods:

    method = eval(m)
    full_copy = full.copy()
    res = cv2.matchTemplate(full_copy,face,method)

    minVal , maxVal , minLoc , maxLoc = cv2.minMaxLoc(res)

    if method in ['cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']:

        top_left = minLoc
    else:
        top_left = maxLoc

    width , height , channels = face.shape

    bottom_right = (top_left[0]+width,top_left[1]+height)
    cv2.circle(full_copy,top_left,20,(255,255,0),-1)
    cv2.rectangle(full_copy,top_left,bottom_right,(255,0,0),5)

    plt.subplot(121)
    plt.imshow(res)
    plt.title('HEATMAP')

    plt.subplot(122)
    plt.imshow(full_copy)
    plt.title('Detected')

    plt.suptitle(m)

plt.show()