import cv2 as cv
import numpy as np

frame = np.zeros((400,400))


while True:

    frame[0:200, 0:200] = 1

    cv.imshow("frame", frame)

    cv.waitKey(0)
    cv.DestroyAllWindows()