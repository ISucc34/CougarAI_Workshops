import cv2 as cv
import numpy as np

height = 640
width = 360


cam = cv.VideoCapture(0)
cam.set(cv.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv.CAP_PROP_FPS, 30)


while True:
    ret, frame = cam.read()

    zero = np.zeros_like(frame) #Creates a list of all zeros with the same shape as frame
    zero[:600, :600] = 255 #Make our region of interest white, this will be what shows up

    ones = np.ones_like(frame) * 255 #multiply by 255 to ensure ones are all white

    ones[:600, :600] = 0 #Make our region of interest black, this region will not show up


    object = cv.bitwise_and(frame,zero)


    cv.imshow("bitwise", object)

    if cv.waitKey(1) == ord('q'):
        break

cv.DestroyAllWindowsxs