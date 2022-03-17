import cv2

image_ul = '../../../images/photo.jpg'

# Charge l'image
image = cv2.imread(image_ul, cv2.IMREAD_UNCHANGED)


# Voir les dimensions de mon image
print(image.shape)
red_channel = [image[:, :, i] = 0 for i in image[:, :, 1]]
green_channel = image[:, :, [1]]
blue_channel = image[:, :, [2]]

#cv2.imwrite('./cv2-red-channel.png', red_channel)

# Afficher image
cv2.imshow('red', red_channel)
cv2.imshow('green', green_channel)
cv2.imshow('blue', blue_channel)

# Le temps d'affichage de l'image 0: infini et n: millisecond
cv2.waitKey(0)
