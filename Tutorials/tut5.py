import cv2 as cv
import numpy as np
import sys

# cap =cv.VideoCapture(0)
cap = cv.imread('balls.png', -1)

while True:
    # ret, frame=cap.read()
    # width=int(cap.get(3))
    # height=int(cap.get(4))
    frame =cap
    hsv=cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lowerblue=np.array([157,255,94])
    upperblue=np.array([177,255,200])
    mask=cv.inRange(hsv, lowerblue, upperblue)

    result = cv.bitwise_and(frame,frame,mask=mask)

    # bgrcolor=np.array([[[255,0,0,0]]])
    # x = cv.cvtColor(bgrcolor , cv.COLOR_BGR2HSV)
    # print(x)
    cv.imshow('result',result)
    # cv.imshow('mask',mask)
    # cv.imshow('img',frame)
    if(cv.waitKey(1)==ord('q')):
        break

cap.release()
cv.destroyAllWindows()
 