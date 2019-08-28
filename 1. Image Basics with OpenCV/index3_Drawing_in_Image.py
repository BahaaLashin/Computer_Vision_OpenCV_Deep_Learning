import numpy as np
import matplotlib.pyplot as plt
import cv2

def display(img):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    ax.imshow(img)


blank_img = np.zeros(shape=(1000,1000,3),dtype=np.int32)

### Draw Rectangle ###

cv2.rectangle(blank_img,pt1=(100,100),pt2=(200,200),color=(0,0,255),thickness=10)

### Draw Circle ###

cv2.circle(img=blank_img,center=(250,250),radius=50,color=(255,0,0),thickness=-1)


### Draw Line ###

cv2.line(blank_img,pt1=(0,0),pt2=(1000,1000),color=(123,145,322),thickness=4)

### put Text ###

font = cv2.FONT_HERSHEY_COMPLEX

cv2.putText(img=blank_img,text='Bahaa Eldin',org=(20,980),fontFace=font,fontScale=2,lineType=cv2.LINE_4,thickness=5,color=(0,255,0))

### Draw Polygans ###

points = np.array([[100,200],[200,300],[300,100]],dtype=np.int32)

points = points.reshape((-1,1,2))

cv2.polylines(img=blank_img,pts=[points],isClosed=True,color=(255,24,232),thickness=5)

### display Image

display(blank_img)