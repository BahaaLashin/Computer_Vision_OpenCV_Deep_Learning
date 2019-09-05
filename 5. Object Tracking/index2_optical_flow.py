import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

ret , frame1 = cap.read()

prevsImg = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

hsv_mask = np.zeros_like(frame1)
hsv_mask[:,:,1] = 255

while True :

    ret , frame2 = cap.read()

    nxtImg = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(prevsImg,nxtImg,None,.5,3,15,3,5,1.2,0)

    ang , mang = cv2.cartToPolar(flow[:,:,0],flow[:,:,1])

    hsv_mask[:,:,0] = mang/2
    hsv_mask[:,:,2] = cv2.normalize(ang,None,0,255,cv2.NORM_MINMAX)

    bgr = cv2.cvtColor(hsv_mask,cv2.COLOR_HSV2RGB)

    cv2.imshow('frame',bgr)
    
    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()


