import cv2 as cv
import numpy as np


cam = cv.VideoCapture(0)

height = 360
width = 640

cam.set(cv.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv.CAP_PROP_FPS, 30)

evt = 0
xpos = 0
ypos = 0




def colorDetect(event, x, y, flag, para):
    global evt 
    global xpos
    global ypos
    if event == cv.EVENT_LBUTTONDOWN:
        evt = event
        xpos = x
        ypos = y
        

cv.namedWindow("frame")
cv.setMouseCallback("frame", colorDetect)


while True:
    ret, frame = cam.read()
    
    frameHSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    cv.imshow("frame", frame)

    if evt == 1:
        print(frame[ypos][xpos])

        color = np.zeros([250,250,3], dtype = np.int8)
        color[:, :] = frame[ypos][xpos]

        cv.putText(color, str(frame[ypos][xpos]), (0,50), cv.FONT_HERSHEY_COMPLEX, 1,(255,255,255),1)
        cv.imshow("BGR color", color)
        
        cv.moveWindow("BGR color", width, 0)
        

        evt = 0
        

    if cv.waitKey(1) == ord('q'):
        break