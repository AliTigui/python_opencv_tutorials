import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])

print(f"top corner value is {image[0][0]}") 
# counting start from top left [y][x] the first is for y and the second is for x
# in opencv the rgb values are bgr
image[0:100,0:100]=(0,0,255)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.imwrite("newimage.jpg", image)
 
