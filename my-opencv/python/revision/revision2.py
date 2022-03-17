import pafy
import cv2

url = "https://www.youtube.com/watch?v=PmJVOzfcILE&t=735s"

makityFan = pafy.new(url)

video = makityFan.getbest(preftype="mp4")

cap = cv2.VideoCapture(video.url)

while True:
    ok, image = cap.read()

    cv2.imshow('image', image/image.max())

    print(image.shape)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
