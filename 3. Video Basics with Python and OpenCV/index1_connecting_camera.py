import cv2
import numpy as np


cap = cv2.VideoCapture(0)


hight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

writer = cv2.VideoWriter('hello.mp4',cv2.VideoWriter_fourcc(*'DIVX'),20,(width,hight))

while True:

    ret , frame = cap.read()
    frame = cv2.medianBlur(frame,15)

    cv2.imshow('Frame',frame)
    writer.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

writer.release()
cap.release()
cv2.destroyAllWindows()