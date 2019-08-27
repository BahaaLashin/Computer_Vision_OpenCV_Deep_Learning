import numpy as np
import cv2

img = cv2.imread('1.jpeg')

while True:

    cv2.imshow('FrameName',img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()