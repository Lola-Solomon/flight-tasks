import numpy as np
import cv2
cap=cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    #determine the location of face with a limitation of 5 faces
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,h,w) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),)
        eyeg=gray[y:y+h,x:x+w]
        eyec=frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(eyeg, 1.3, 5)
        for (xe,ye,he,we)in eyes:
            cv2.rectangle(eyec,(xe,ye),(xe+we,ye+he),(0,0,255),)
    cv2.imshow('frame',frame)    
    if cv2.waitKey(1) == ord('x'):
        break
cap.release()
cv2.destroyAllWindows()   