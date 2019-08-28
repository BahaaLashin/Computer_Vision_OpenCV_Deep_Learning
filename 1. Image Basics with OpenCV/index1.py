import numpy as np
import matplotlib.pyplot as plt
import cv2
%matplotlib qt

def display(img):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    ax.imshow(img)


### READ IMAGE ####
img = cv2.imread('1.jpeg')


### CONVERT IMAGE TO RGB ####

img_converted = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

### Convert image in gray ###

img_gray = cv2.imread('1.jpeg',cv2.IMREAD_GRAYSCALE)

### resize image to new size ###

img_resized = cv2.resize(img,(200,500))

h_retio = .5
w_retio = .5

img_resized_2 = cv2.resize(img,(0,0),img,w_retio,h_retio)

### Flip Image ###

flip_image = cv2.flip(img,-1)

#### Write Image ###

img_write = cv2.imwrite('new_image.jpg',flip_image)

if img_write:
    print('Image has been saved')

### SHOW IMAGE ####

display(flip_image)