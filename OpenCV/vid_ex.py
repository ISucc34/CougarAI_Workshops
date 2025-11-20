import cv2 as cv

def video():
    cam = cv.VideoCapture(0) #0 is the index of array of cameras connected to your device
    #cam = cv.VideoCapture("Cat.mp4") #Also accepts video files

    while True:
        ret, frame = cam.read()
        cv.imshow("webcam", frame)

        if cv.waitKey(1) == ord('q'):
            break
    cv.DestroyAllWindows()


video()