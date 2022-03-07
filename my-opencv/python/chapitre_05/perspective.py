import cv2
import numpy as np

width, heigth = 350, 400

pts1 = np.float32([[646, 44], [1186, 44], [640, 387], [1185, 388]])
pts2 = np.float32([[0, 0], [width, 0], [0, heigth], [width, heigth]])

matrice = cv2.getPerspectiveTransform(pts1, pts2)


image_url = '../../../images/card.png'

image = cv2.imread(image_url)

image2 = cv2.warpPerspective(image, matrice, (width, heigth))
print(image.shape)

cv2.imshow('card', image)
cv2.imshow('card 2', image2)

cv2.waitKey(0)
