# simple image proccessing (shifting translate rotation resizing fliping croping)

import numpy as np
import argparse
import imutils as im
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyWindow("Original")

# translation to image
shifted = im.translation(image,25,50)
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)
cv2.destroyWindow("Shifted Down and Right")

shifted = shifted = im.translation(image,-50,-90)
cv2.imshow("Shifted Up and Left", shifted)
cv2.waitKey(0)
cv2.destroyWindow("Shifted Up and Left")

# rotation to image
#methode 2
rotated = im.rotate(image, 45, scale=1.0)
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey(0)
cv2.destroyWindow("Rotated by 45 Degrees")

rotated = im.rotate(image, -90, scale=1.0)
cv2.imshow("Rotated by -90 Degrees", rotated)
cv2.waitKey(0)
cv2.destroyWindow("Rotated by -90 Degrees")

#methode 2
imager=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Image", imager)
cv2.waitKey(0)
cv2.destroyWindow("Image")

#resize image
resized = im.resize(image, height = 100)
cv2.imshow("resized", resized )
cv2.waitKey(0)
cv2.destroyWindow("resized")

#flipping image
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)
cv2.waitKey(0)

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)
cv2.waitKey(0)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Croping
# with croping we take part of the image
crop=image[100:150,200:225]
cv2.imshow("Croped", crop)
cv2.waitKey(0)
cv2.imwrite("croped.png",crop)