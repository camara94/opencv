import cv2

image_ul = '../../../images/photo.jpg'

# Charge l'image
image = cv2.imread(image_ul)

# Voir les dimensions de mon image
print(image.shape)

# comment redimensionner une image
imageRedimensionne = cv2.resize(image, (1000, 500))
print(imageRedimensionne.shape)

imageCrop = image[0:80, 100: 220]

# Afficher image
cv2.imshow('ma premiere image', image)
cv2.imshow('image redimensionner', imageCrop)

# Le temps d'affichage de l'image 0: infini et n: millisecond
cv2.waitKey(0)
