import cv2

# url de la video
video_url = '../../video/paris.mp4'

# crée un objet video
video = cv2.VideoCapture(video_url)

# je vais faire une boucle pour lire la video
while True:
    i = 0
    # je vais decomposer la video en plusieurs image
    sucess, image = video.read()

    i = i + 1
    print(image.shape, i)

    cv2.imshow(f'image {i}', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
