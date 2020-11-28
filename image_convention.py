import cv2
import numpy as np

img = cv2.imread('resource/Messi.jpg')
print(img.shape)

# image resize
resize_image = cv2.resize(img,(350,350))
print(resize_image.shape)

# crop image
image_crop = img[250:500,250:500]

cv2.imshow("Messi",img)
cv2.imshow("Messi 350*350",resize_image)
cv2.imshow("crop 350*350",image_crop)

cv2.waitKey(0)