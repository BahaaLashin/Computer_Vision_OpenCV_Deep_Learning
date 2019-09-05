import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

ret , frame = cap.read()

cascade_classifier = cv2.CascadeClassifier('faceFront.xml')

clf = cascade_classifier.detectMultiScale(frame)

(x,y,w,h) = tuple(clf[0])

track_window = (x,y,w,h)

rio = frame[y:y+h,x:x+w]

hsv_rio = cv2.cvtColor(rio,cv2.COLOR_BGR2HSV)

rio_hist = cv2.calcHist(hsv_rio,[0],None,[180],[0,180])

cv2.normalize(rio_hist,rio_hist,0,255,cv2.NORM_MINMAX)

term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)

while True:

    ret , frame1 = cap.read()

    if ret == True:

        hsv = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

        dst = cv2.calcBackProject([hsv],[0],rio_hist,[0,180],1)
        ''''
        ret , track_window = cv2.meanShift(dst,track_window,term_crit)

        x,y,w,h = track_window

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,255,0),6)
        '''
        ret , track_window = cv2.CamShift(dst,track_window,term_crit)
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)

        cv2.polylines(frame1,[pts],True,(255,0,0),5)

        cv2.imshow('frame',frame1)
        
        if cv2.waitKey(10) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()