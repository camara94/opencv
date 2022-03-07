import cv2

cam = cv2.VideoCapture(0)

cam.set(3, 600)
cam.set(4, 600)
cam.set(10, 300)

while True:

    success, image = cam.read()

    print(image.shape)

    cv2.imshow('image', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
