import cv2
import numpy as np

image_url = '../../../images/card.png'

image = cv2.imread(image_url)
print(image.shape)

cv2.imshow('card', image)

cv2.waitKey(0)
