import cv2
import numpy as np

img = np.zeros((712,812,3),np.uint8)
img1 = np.zeros((712,812,3),np.uint8)
img2 = np.zeros((712,812,3),np.uint8)
print(img.shape)

img[:] = 255,0,0 # change hole image color
# img2[100:250,20:251] = 255,0,0 # color crop

cv2.line(img,(100,0),(500,712),(0,255,125),1)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,125),1) # line
cv2.rectangle(img,(100,50),(250,300),(0,0,254),1) # rectangle
cv2.rectangle(img,(300,150),(550,500),(0,0,254),cv2.FILLED) # filled rectangle
cv2.circle(img,(700,250),100,(255,200,2),cv2.FILLED) # filled circle
cv2.circle(img,(700,550),100,(0,0,2),5) # circle
cv2.putText(img, " ONI ",(350,300),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),5) # text view in image
#
cv2.imshow("Messi",img)
# cv2.imshow("img1",img1)
# cv2.imshow("img2",img2)



cv2.waitKey(0)