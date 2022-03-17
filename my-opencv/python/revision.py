import cv2

path = '../../images/photo.jpg'

image = cv2.imread(path)
image2 = cv2.imread(path)

image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)
image2 = cv2.resize(image2, None, fx=2, fy=2)


print(image.shape)
print(image2.shape)

cv2.imshow('image', image)
cv2.imshow('image 2', image2)

cv2.waitKey(0)
