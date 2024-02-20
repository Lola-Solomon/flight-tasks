import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    #getting the width of the frame 
    width=int(cap.get(3))
    #getting the height of the frame 
    height=int(cap.get(4))
    #creating a numpy array of zeros and shaping it as the frame
    img=np.zeros(frame.shape,np.uint8)
    #creating a new var to make a smaller frame 
    small_frame=cv2.resize(frame,(0,0),fx=.5,fy=.5)
    #the top left
    img[:height//2,:width//2]=small_frame
    #the bottom left
    img[height//2:,:width//2]=small_frame
    #the top right
    img[:height//2,width//2:]=small_frame
    #the bottom right
    img[height//2:,width//2:]=small_frame
    cv2.imshow('frame',img)
    #if i click 'x' the video will close
    if cv2.waitKey(1) == ord('x'):
        break
cap.release()
cv2.destroyAllWindows()   