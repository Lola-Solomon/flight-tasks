import numpy as np
import cv2
img=cv2.resize(cv2.imread(r'D:\flight_tasks\visionn\flight-tasks\opencv\soccer_practice.jpg',0),(0,0),fx=.8,fy=.8)
temp=cv2.resize(cv2.imread(r'ball.PNG',0),(0,0),fx=.8,fy=.8)
h,w=temp.shape
#trying multiple methods because not all of them work
methods=[cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]
for method in methods:
    img1=img.copy()
    #the temo sweeps the img to find if it matches 
    res=cv2.matchTemplate(img1,temp,method)
    #location of the temp in the main img
    min_v,max_v,min_loc,max_loc=cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location=min_loc
    else:
        location=max_loc 
    
    bottom_r=location[0]+w,location[1]+h
    cv2.rectangle(img1,location,bottom_r,255,5)
    cv2.imshow('img',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

