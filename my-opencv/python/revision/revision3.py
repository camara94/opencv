import cv2

cam = cv2.VideoCapture(0)


while True:
    ok, image = cam.read()
    image = cv2.resize(image, None, fx=2, fy=2)
    cv2.imshow('ma camera', image[:, :, 2])
    print(image.shape)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
