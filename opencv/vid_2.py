import cv2
#read the image by writing its path ...-1 will load a color image with transparency neglection
img=cv2.imread('logo.jpg',-1)
#slice a part of image and paste it in the same image
tagg=img[500:700,600:900]
img[100:300,650:950]=tagg
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()