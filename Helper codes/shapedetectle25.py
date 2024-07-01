import cv2 as cv
import numpy as np

img =cv.imread('balls.png')
imggrey=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thrash=cv.threshold(imggrey,240,255,cv.THRESH_BINARY)

contours, _ = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01* cv.arcLength(contour, True), True)
    cv.drawContours(img, [approx], 0, (0,0,255), 5)
    x=approx.ravel()[0]
    y=approx.ravel()[1]
    if len(approx) == 3:
        cv.putText(img, "triangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, [0,255,255])
    elif len(approx) == 4:
        x,y,w,h = cv.boundingRect(approx)
        aspectratio= float (w)/h
        print(aspectratio)
        if aspectratio >= 0.95 and aspectratio<=1.05:
            cv.putText(img, "square", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, [0,255,255])
        else:
            cv.putText(img, "rectangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, [0,255,255])
    elif len(approx) == 5:
        cv.putText(img, "pentagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, [0,255,255])
    elif len(approx) == 10:
        cv.putText(img, "star", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, [0,255,255])
    else:
        cv.putText(img, "circle", (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, [0,255,255])

cv.imshow("shapes",img)
cv.waitKey(0)
cv.destroyAllWindows()