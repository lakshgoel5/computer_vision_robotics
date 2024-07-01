import cv2 as cv
import numpy as np

cap =cv.VideoCapture('VID-20230605-WA0047.mp4')

while True:
    ret, frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    smaller_frame=cv.resize(frame,(0,0), fx=0.5,fy=0.5)
    image=np.zeros(frame.shape, np.uint8)
    image[:height//2, :width//2]=smaller_frame
    image[height//2:, :width//2]=cv.rotate(smaller_frame, cv.ROTATE_180)
    image[:height//2, width//2:]=cv.rotate(smaller_frame, cv.ROTATE_180)
    image[height//2:, width//2:]=smaller_frame

    cv.imshow('frame',image)
    if(cv.waitKey(90)==ord('q')):
        break

cap.release()
cv.destroyAllWindows()