import cv2
import numpy as np 

cap=cv2.VideoCapture(0)

while True:
    r,frame=cap.read()
    gr=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    co=cv2.goodFeaturesToTrack(gr,1000000,0.025,1)
    co=np.int0(co)
    for i in co:
        x,y=i.ravel()
        frame=cv2.circle(frame,(x,y),5,(255,0,0),-1)
    cv2.imshow("contoure",frame)
    cv2.imshow("grey",gr)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()