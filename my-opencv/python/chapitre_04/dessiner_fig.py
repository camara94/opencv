import cv2

import numpy as np

image = np.zeros((512, 512, 3), np.uint8)

image[100:200, 50:400] = 25, 0, 180

cv2.line(image, (0, 0), (512, 512), (0, 252, 0), 3)
cv2.line(image, (0, 512), (512, 0), (0, 252, 0), 3)

cv2.line(image, (0, 256), (512, 256), (512, 252, 0), 3)

cv2.rectangle(image, (0, 0), (512, 256), (512, 252, 0), 4)

cv2.circle(image, (256, 256), 45, (0, 0, 45), 4)

cv2.imshow('dessiner une fig', image)

cv2.putText(image, "LABY DAMARO CAMARA", (300, 200),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

cv2.waitKey(0)
