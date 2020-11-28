import cv2
import numpy as np

# import opencv computer version
print('package Imported')
img = cv2.imread('resource/Messi.jpg')
karnel  = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,100,100);
imaDialation = cv2.dilate(imgCanny,karnel,iterations=1)

# iamge view
cv2.imshow("Messi Output",imgGray)
cv2.imshow("Messi Blur",imageBlur)
cv2.imshow("Messi canny",imgCanny)
cv2.imshow("Messic dialation",imaDialation)
cv2.waitKey(0)
