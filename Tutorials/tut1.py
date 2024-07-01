import cv2 as cv
import sys
import random

img = cv.imread('Python.png', -1)

tag = img[100:170,120:190]
img[200:270,200:270] = tag
print(img.shape)
print(img)
cv.imshow('Image',img)
cv.waitKey(0)
cv.destroyAllWindows()