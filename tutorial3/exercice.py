import numpy as np
import cv2
canvas = np.zeros((300, 300, 3), dtype = "uint8")
f=True
for i in range(0,300,20):
    for j in range(0,300,20):
        if f:
            cv2.rectangle(canvas, (i,j), (i+20, j+20), (0,0,255),-1)
            f=False
        else:
            f=True
cv2.circle(canvas, (300//2,300//2), 50, (0,255,0), -1) # draw the circle
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)