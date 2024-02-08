import numpy as np
import cv2
# in this tutorial wewill see masking and ditecting color
cap=cv2.VideoCapture(0)
while True:
    res,frame=cap.read()
    l= np.array([80, 0, 0])
    h = np.array([120, 240, 240])
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,l,h)
    frame=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1)==ord("q"):
        break

cv2.destroyAllWindows()
cap.release()