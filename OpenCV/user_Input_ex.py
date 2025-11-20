import cv2 as cv

height = 640
width = 360

cam = cv.VideoCapture(0)
cam.set(cv.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv.CAP_PROP_FPS, 30)

evt = 0
pos = 0


def mouseInput(event, x, y, flags, params): #what did the mouse do(event), position of mouse click(x,y), special keys like ctrl(flags)
    global evt
    global pos #made these global for other functions to access
    if event == cv.EVENT_LBUTTONDOWN:
        evt = event
        pos = (x,y)
    if event == cv.EVENT_LBUTTONUP:
        evt = event
        pos = (x,y)


cv.namedWindow("Cam")
cv.setMouseCallback("Cam", mouseInput) #Window for input, function to call, passes 5 values as parameters 

while True:
    ret, frame = cam.read()
    
    if evt == cv.EVENT_LBUTTONDOWN:
        print(pos)
        evt = 0 #Set to 0 when done to prevent printing forever, comment it out to try
    if evt == cv.EVENT_LBUTTONUP:
        print(pos)
        evt = 0

    cv.imshow("Cam", frame)

    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()