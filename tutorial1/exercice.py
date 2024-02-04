#rotate image
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.imwrite("retated_image.jpg", image)