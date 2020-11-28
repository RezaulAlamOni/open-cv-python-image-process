import cv2
# import opencv computer version
print('package Imported')
img = cv2.imread('resource/Messi.jpg')

# iamge view
cv2.imshow("Messi Output",img)
cv2.waitKey(0)
