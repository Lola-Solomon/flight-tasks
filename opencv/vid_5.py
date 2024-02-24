import cv2 
import numpy as np
cap=cv2.VideoCapture(0)
while True :
    ret,frame=cap.read()
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #the color boundraies in the array
    low_blu=np.array([110,50,50])
    up_blu=np.array([130,255,255])
    #mask is array of ones and zeros the detected color in the specified img is one 
    mask=cv2.inRange(hsv,low_blu,up_blu)
    #we take the color from the source img 
    result=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',result)

    if cv2.waitKey(1)==ord('x'):
        break
cap.release()
cv2.destroyAllWindows()    

