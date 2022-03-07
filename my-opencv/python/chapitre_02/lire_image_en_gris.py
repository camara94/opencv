import cv2
import matplotlib.pyplot as plt

image_url = '../../../images/photo.jpg'

image = cv2.imread(image_url)

imageGris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageGris = imageGris / 255*2

print(image.shape)
print(imageGris)

cv2.imshow('image grise', imageGris)
cv2.imshow('image en couleur', image)
cv2.waitKey(0)
