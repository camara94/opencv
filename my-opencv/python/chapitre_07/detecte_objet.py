import cv2
import numpy as np


def empty():
    pass


image_url = '../../../images/photo.jpg'

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars', 640, 340)
cv2.createTrackbar('Hue Min', 'Trackbars', 0, 179, empty)

image = cv2.imread(image_url)

imagesHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('image reel', image)
cv2.imshow('image hsv', imagesHSV)

cv2.waitKey(0)
