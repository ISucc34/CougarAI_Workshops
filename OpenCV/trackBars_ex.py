import cv2 as cv

cam = cv.VideoCapture(0)

width  = 640
height = 360
startVal = 320

cam.set(cv.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv.CAP_PROP_FPS, 30)

def callback(val):
    print(val)

#Name of your slider, window to insert trackbar, start value (not min val), max value, function to call
cv.namedWindow('Trackbars')
cv.createTrackbar('X', 'Trackbars', startVal, 1920, callback)




def trackbars():
    cam = cv.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        cv.imshow("Cam", frame)
    
        if cv.waitKey(1) == ord('q'):
            break

    cv.DestroyAllWindows()

if __name__ == "__main__":
    trackbars()