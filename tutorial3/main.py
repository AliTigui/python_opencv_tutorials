# drawing shaps in image 
import numpy as np
import cv2

# draw lines
canvas = np.zeros((300, 300, 3), dtype = "uint8")
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw rectangle
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1) # negative value to thickness mean fill rectangle with blue 
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw circle
canvas2 = np.zeros((300, 300, 3), dtype = "uint8")
(centerX, centerY) = (canvas2.shape[1] // 2, canvas2.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(canvas2, (centerX, centerY), r, white) # r is radius

cv2.imshow("Canvas", canvas2)
cv2.waitKey(0)

# draw many random circle 
canvas3 = np.zeros((300, 300, 3), dtype = "uint8")
for i in range(0, 25):
    radius = np.random.randint(5, high = 200) # get random value of radius
    color = np.random.randint(0, high = 256, size = (3,)).tolist() # get random value for color
    pt = np.random.randint(0, high = 300, size = (2,)) # get random value for position
    cv2.circle(canvas3, tuple(pt), radius, color, -1) # draw the circle

cv2.imshow("Canvas", canvas3)
cv2.waitKey(0)