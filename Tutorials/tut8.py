import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
face_cascade= cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade= cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret,frame= cap.read()

    gray= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, 1.3, 5) #return faces in terms of position
    for(x ,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 5)
        roi_gray=gray[ y:y+h,x:x+w]
        roi_color=frame[ y:y+h, x:x+w,]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.3,5)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color, (ex,ey),(ex+ew, ey+eh), (0,255,0),5) #frame not passed as you are just looking at face

    cv.imshow('frame', frame)

    if cv.waitKey(1)==ord('q'):
        break

cap.release()
cv.destroyAllWindows()