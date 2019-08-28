import numpy as np
import matplotlib.pyplot as plt
import cv2

###### Variables ####

drawing = False
ix ,iy = 0,0

###### Function ####

def draw_rectangle(event,x,y,flags,params):

    global drawing,ix,iy

    if event == cv2.EVENT_LBUTTONDOWN:
        ix,iy=x,y
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:

        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(66,66,66),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img,(ix,iy),(x,y),(66,66,66),-1)
        drawing = False

#### Show Image ####


img =np.zeros((1000,1000,3),np.uint8)

cv2.namedWindow(winname='halla')
cv2.setMouseCallback('halla',draw_rectangle)

while True:

    cv2.imshow('halla',img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()