import cv2
import numpy as np

image_url = '../../../images/photo.jpg'

image = cv2.imread(image_url)
#image = image.resize(image, (400, 300))

imageVerticales = np.vstack((image, image))
imageHorizontales = np.hstack((image, image))

cv2.imshow('grouper image v', imageVerticales)
cv2.imshow('grouper image h', imageHorizontales)
cv2.waitKey(0)
