import cv2
import matplotlib.pyplot as plt
import numpy as np

kernel = np.ones((5, 5), np.uint8)

image_url = '../../../images/photo.jpg'

image = cv2.imread(image_url)

cannyImage = cv2.Canny(image, 200, 200)

imageDialet = cv2.dilate(cannyImage, kernel, iterations=1)
imageErode = cv2.erode(imageDialet, kernel, iterations=1)

print(cannyImage.shape)

cv2.imshow('canny', cannyImage)
cv2.imshow('dialet', imageDialet)
cv2.imshow('erode', imageErode)
cv2.waitKey(0)
