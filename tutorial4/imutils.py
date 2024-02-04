import numpy as np
import cv2

def translation(image,tx,ty): 
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape
    [0]))
    return shifted
def rotate(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated
def resize(image, width = None, height = None, x=None,y=None,inter = cv2.
INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None and x is None and y is None:
        return image

    if width is None and x is None and y is None:
        r = height / float(h)
        dim = (int(w * r), height)

    elif height is None and x is None and y is None :
        r = width / float(w)
        dim = (width, int(h * r))
    else:
        dim = (0, 0)
        resized = cv2.resize(image, dim, fy=y,fx=x,interpolation = inter)
        return resized
    resized = cv2.resize(image, dim, interpolation = inter)
    return resized