import pafy
import cv2

url = "https://www.youtube.com/watch?v=D8QSezkMGZo&list=RDMM9gK3j6m0o1Q&index=4"

video_detail = pafy.new(url)
video = video_detail.getbest(preftype="mp4")

print(video.url)
