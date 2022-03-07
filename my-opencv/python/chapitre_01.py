import cv2
# Comment lire une image

url_image = "photo.jpg"

image = cv2.imread(url_image)
# pour afficher l'images
cv2.imshow("Notre sortie", image)
print(image.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
