import cv2

image_ul = '../../../images/photo.jpg'

# Charge l'image
image = cv2.imread(image_ul)

# Voir les dimensions de mon image
print(image.shape)

# Afficher image
cv2.imshow('ma premiere image', image)

# Le temps d'affichage de l'image 0: infini et n: millisecond
cv2.waitKey(2000)
