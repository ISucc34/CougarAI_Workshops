import cv2 as cv
import numpy as np 

cam = cv.VideoCapture(0)

height = 360
width = 640

cam.set(cv.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv.CAP_PROP_FPS, 30)

while True:
    ret, frame = cam.read()

    frameHSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowerbound = np.array([0,0,0])
    upperbound = np.array([100,100,100])

    frameHSV = cv.inRange(frameHSV, lowerbound, upperbound)

    cv.imshow("frame", frameHSV)

    if cv.waitKey(1) == ord('q'):
        break