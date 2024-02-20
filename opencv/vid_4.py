import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    #getting the width of the frame 
    width=int(cap.get(3))
    #getting the height of the frame 
    height=int(cap.get(4))
    #lines
    img=cv2.line(frame,(0,0),(width,height),(0,0,255),2)
    img=cv2.line(frame,(50,30),(0,height),(70,0,50),5)
    #circle
    img=cv2.circle(frame,(width//2,height//2),60,(80,0,150),-1)
    #recatngle
    img=cv2.rectangle(frame,(20,30),(60,50),(70,255,50),5)
    #line
    font=cv2.FONT_HERSHEY_COMPLEX
    img=cv2.putText(frame,'HI HI CAPTAIN',(50,200),font,2,(255,0,0),3,cv2.LINE_AA)
    cv2.imshow('frame',img)
    #if i click 'x' the video will close
    if cv2.waitKey(1) == ord('x'):
        break
cap.release()
cv2.destroyAllWindows() 