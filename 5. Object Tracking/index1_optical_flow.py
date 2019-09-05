import numpy as np
import cv2
import matplotlib.pyplot as plt
corner_track_params = dict(maxCorners=10,qualityLevel = .3 , minDistance = 7 , blockSize= 7)
lk_params = dict(winSize=(200,200),maxLevel = 2, criteria= (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT , 10,0.003))

cap = cv2.VideoCapture(0)

ret , init_frame = cap.read()

init_frame_gray = cv2.cvtColor(init_frame,cv2.COLOR_BGR2GRAY)

init_good_features = cv2.goodFeaturesToTrack(init_frame_gray,mask=None,**corner_track_params)

mask = np.zeros_like(init_frame)

while True :

    ret , frame = cap.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    second_good_features , status , err = cv2.calcOpticalFlowPyrLK(init_frame_gray,frame_gray,init_good_features,None,**lk_params)

    good_prev = second_good_features[status == 1]
    good_next = init_good_features[status == 1]

    for i ,(new,prev) in enumerate(zip(good_next,good_prev)):

        x_new , y_new = new.ravel()
        x_prev , y_prev = prev.ravel()

        cv2.line(mask,(x_new,y_new),(x_prev,y_prev),(255,255,255),4)
        cv2.circle(frame,(x_new,y_new),9,(255,0,255),-1)

    img = cv2.add(frame,mask)
    cv2.imshow('frame',img)

    if cv2.waitKey(10) & 0xFF == 27:
        break

    init_frame_gray = frame_gray.copy()
    init_good_features = good_prev.reshape(-1,1,2)
cap.release()
cv2.destroyAllWindows()