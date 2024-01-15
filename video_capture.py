import cv2
import matplotlib as plt

cam = cv2.VideoCapture(0)
cv2.namedWindow('test')

while True:
    ret, frame = cam.read()
    if not ret:
        print('Failed to grab frame')
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Capturing', frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        break

cam.release()
cv2.destroyAllWindows()