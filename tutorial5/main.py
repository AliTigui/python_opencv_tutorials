import numpy as np 
import cv2
import ultraimport
rotate = ultraimport('__dir__/../tutorial4/imutils.py', 'rotate')

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    canva=np.zeros(frame.shape,np.uint8)
    smaller_frame=cv2.resize(frame,(0,0),fy=0.5,fx=0.5)
    h=frame.shape[0]
    w=frame.shape[1]
    canva[0:h//2,0:w//2]=cv2.flip(smaller_frame,1)
    canva[0:h//2,w//2:]=rotate(smaller_frame,180)
    gray=smaller_frame.copy()
    for i in range(h//2):
        for j in range(w//2):
            g=sum(smaller_frame[i][j])//3
            gray[i][j]=(g,g,g)
    canva[h//2:,0:w//2]=gray
    canva[h//2:,w//2:]=smaller_frame
    cv2.imshow("camera",canva)
    if cv2.waitKey(1)==ord("q"):
        break
cv2.destroyWindow("camera")
cap.release()