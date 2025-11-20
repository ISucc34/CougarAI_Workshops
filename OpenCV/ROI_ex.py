import cv2 as cv

height = 640
width = 360

cam = cv.VideoCapture(0)
cam.set(cv.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv.CAP_PROP_FPS, 10)

while True:
    ret, frame = cam.read()

    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #(<img to convert>, conversion type)

    frameROI = frame[0:height, 0:width] #The region we want

    #Implementing ROI into the grayFrame

    #grayFrame[0:height, 0:width] = frameROI #ERROR, because grayscale is 3x3x1 not 3x3x3 of the ROI 3x3x3

    frameBGR = cv.cvtColor(grayFrame, cv.COLOR_GRAY2BGR) #Since we converted to BGR from grayframe it will stay gray
    frameBGR[0:height, 0:width] = frameROI


    cv.imshow("Frame", frameBGR)


    if cv.waitKey(1) == ord('q'):
        break

cv.DestroyAllWindows()