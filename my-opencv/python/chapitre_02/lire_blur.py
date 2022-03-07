import cv2
import matplotlib.pyplot as plt

image_url = '../../../images/photo.jpg'

image = cv2.imread(image_url)

imageGris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(imageGris, (7, 7), 10)

cv2.imshow('image bruite', imageBlur)
cv2.waitKey(0)
