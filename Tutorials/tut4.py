import cv2 as cv
import numpy as np

cap =cv.VideoCapture('VID-20230605-WA0047.mp4')

while True:
    ret, frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    img = cv.line(frame,(0,0), (width, height),(255,0,0), 10)
    img = cv.line(img,(0,height), (width, 0),(0,255,0), 5)
    img = cv.rectangle(img,(100,100), (200,200),(120,120,255), -1)
    font =cv.FONT_HERSHEY_SIMPLEX
    img=cv.putText(img,'Laksh',(100,height-400),font,1.5,(0,5,5),7,cv.LINE_AA)
    cv.imshow('frame',frame)
    if(cv.waitKey(90)==ord('q')):
        break

cap.release()
cv.destroyAllWindows()