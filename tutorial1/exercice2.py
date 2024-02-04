#resize image
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image1=cv2.resize(image,(400,400))
image2=cv2.resize(image,(0,0),fx=0.5,fy=0.5)
cv2.imshow("Image", image1)
cv2.waitKey(0)
cv2.imwrite("resizedimage.jpg", image1)
cv2.imshow("Image", image2)
cv2.waitKey(0)
cv2.imwrite("resizedimage2.jpg", image2)