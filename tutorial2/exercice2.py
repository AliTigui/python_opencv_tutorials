# we will make image gray
# in this exemple we will try flip piture
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])

print(f"top corner value is {image[0][0]}") 

w=image.shape[1]
h=image.shape[0]
for i in range(h):
    for j in range(w):   
        g=sum(image[i][j])/3
        image[i][j]=(g,g,g)



cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.imwrite("newimage.jpg", image)