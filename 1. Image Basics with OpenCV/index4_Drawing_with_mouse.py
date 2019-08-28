import numpy as np
import cv2
import matplotlib.pyplot as plt




###############################
########## Function ###########
###############################



def draw_Circle(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,color=(0,255,9),thickness=-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),10,color=(0,0,255),thickness=-1)





cv2.namedWindow(winname='Man in Black')
cv2.setMouseCallback('Man in Black',draw_Circle)



img = np.zeros((1000,1000,3),dtype=np.uint8)

while True:

    cv2.imshow('Man in Black',img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()