import numpy as np
import cv2
import matplotlib.pyplot as plt

full = cv2.imread('5.jpg',0)
part = cv2.imread('5r.jpg',0)

sift =  cv2.xfeatures2d.SIFT_create()

