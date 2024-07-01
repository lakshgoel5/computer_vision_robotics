import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow("track")
cv.createTrackbar("LH", "track", 0 , 255, nothing)
cv.createTrackbar("LS", "track", 0 , 255, nothing)
cv.createTrackbar("LV", "track", 0 , 255, nothing)

cv.createTrackbar("UH", "track", 255 , 255, nothing)
cv.createTrackbar("US", "track", 255 , 255, nothing)
cv.createTrackbar("UV", "track", 255 , 255, nothing)

while True:
    frame=cv.imread('target.jpeg')

    hsv=cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lh=cv.getTrackbarPos("LH", "track")
    ls=cv.getTrackbarPos("LS", "track")
    lv=cv.getTrackbarPos("LV", "track")

    uh=cv.getTrackbarPos("UH", "track")
    us=cv.getTrackbarPos("US", "track")
    uv=cv.getTrackbarPos("UV", "track")

    lowerblue=np.array([lh,ls,lv])
    upperblue=np.array([uh,us,uv])

    mask = cv.inRange(hsv, lowerblue, upperblue)

    result = cv.bitwise_and(frame,frame, mask=mask)

    cv.imshow("frame",frame)
    cv.imshow("mask",mask)
    cv.imshow("result",result)

    key = cv.waitKey(1)
    if key==27:
        break

cv.destroyAllWindows()