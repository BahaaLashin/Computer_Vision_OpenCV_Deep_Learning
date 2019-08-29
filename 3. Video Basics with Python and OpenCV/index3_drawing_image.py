import cv2
import numpy as np
import time


img = cv2.VideoCapture(0)


height = int(img.get(cv2.CAP_PROP_FRAME_HEIGHT))
width  = int(img.get(cv2.CAP_PROP_FRAME_WIDTH))

while True:

    ret , frame = img.read()

    cv2.rectangle(frame,(height-200,width-200),(int(height/2),int(width/2)),color=(255,255,255),thickness=5)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


img.release()
cv2.destroyAllWindows()