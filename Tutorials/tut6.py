import cv2 as cv
import numpy as np

img =cv.imread('chessboard.png')
img=cv.resize(img,(0,0), fx=0.75, fy=0.75)
##img=cv.cvtColor(img,cv.COLOR_BGR2GRAY) this modified as corners were also white in final image
##modified to
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

corners= cv.goodFeaturesToTrack(gray,100,0.01, 10)
corners=np.intp(corners)

for corner in corners:
    x,y=corner.ravel() ## x is assigned left value, y right value of flattened array
    cv.circle(img, (x,y), 5, (255,0,0), -1)

for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1=tuple(corners[i][0]) ##tuple function converts array into point
        corner2=tuple(corners[j][0])
        color=tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3))) ##shorcut as compared to what we did earlier
        #but this returns a 32 or 64 bit intiger but we want 8 bit intiger
        #therefore use map, basically typecast
        #map convert one array to another, then we used tuple function
        cv.line(img, corner1, corner2, color, 1)

cv.imshow('Frame',img)
cv.waitKey(0)
cv.destroyAllWindows()