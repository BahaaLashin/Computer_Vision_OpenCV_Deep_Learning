import cv2
import matplotlib.pyplot as plt
import numpy as np
import time
cap = cv2.VideoCapture(0)

ix , iy = 0 , 0
sx , sy = 0 , 0
first_click = False
second_click = False
top_left = False
right_bottom = False
def draw_rectangle(event,x,y,flags,params):
    global ix,iy,first_click , second_click,sx,sy,top_left,right_bottom
    cv2.circle(frame,(x,y),50,(255,0,0),thickness=-1)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(frame,(x,y),50,(255,0,0),thickness=-1)
        if first_click == False:

            top_left = True
            ix = x
            iy = y
            first_click = True

        elif second_click == False:
            right_bottom = True
            sx = x
            sy = y
            second_click = True
        elif second_click == True & first_click == True:
            second_click = False
            first_click = False





cv2.namedWindow(winname='my_frame')
cv2.setMouseCallback('my_frame',draw_rectangle)


while True:

    ret ,frame = cap.read()


    if second_click == True:

        cv2.rectangle(frame,(ix,iy),(sx,sy),(255,255,255),thickness=5)
        cv2.circle(frame,(sx,sy),10,(255,0,255),thickness=-1)
    if first_click == True:
      cv2.circle(frame,(ix,iy),10,(255,0,255),thickness=-1)

    cv2.imshow('my_frame',frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
