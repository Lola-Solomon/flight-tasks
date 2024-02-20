import cv2
#read the image by writing its path ...-1 will load a color image with transparency neglection
img=cv2.imread('th.jpg',-1)
#resize the image to half the size
img=cv2.resize(img,(0,0),fx=.5,fy=.5)
# rotate the image 90 clockwise
img=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
#save the img after modification in new path
cv2.imwrite('newimg.jpg',img)
#show the image in window
cv2.imshow('image',img)
#the window will be opend till we press any key
cv2.waitKey(0)
cv2.destroyAllWindows()
