import cv2
# video from directory
cap = cv2.VideoCapture("resource/oni.mp4")
# Open webcam
# cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,440)

while True:
    success, img = cap.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0 == ord('q'):
        break
