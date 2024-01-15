import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow('test')

while True:
    ret, frame = cam.read()
    if not ret:
        print('Failed to grab frame')
        break

    cv2.imshow('Capturing', frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        break

cam.release()
cv2.destroyAllWindows()