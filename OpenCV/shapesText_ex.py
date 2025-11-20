import cv2 as cv
import numpy as np

height = 1280
width = 720
img = np.zeros((400,400))


def Circles():

    #center = (400/2, 400/2) #(row, column)
    center = (int(400/2), int(400/2)) #(row, column)
    radius = 100
    color = (1)
    thickness =-1 #-1 fills in the circle

    cv.circle(img, center, radius, color, thickness) 
    cv.imshow("circle", img)
    cv.waitKey(0)
        
def Rectangles():
    point_1 = (0, 200) #(row, column) upper right
    point_2 = (200, 0) #(row, column) bottom left
    color = (1) 
    thickness = -1 #-1 fills in the rectangle

    cv.rectangle(img, point_1, point_2, color, thickness) 

    cv.imshow("rect", img)
    cv.waitKey(0)

def text():
    txt = "Hello World!"
    font = cv.FONT_HERSHEY_COMPLEX
    position = (100,100) #Upper left corner in (row, column)
    color = (1)
    thickness = 2
    size = 1


    cv.putText(img, txt, position, font, size, color, thickness)
    cv.imshow("text", img)
    cv.waitKey(0)

def Vid():
    cam = cv.VideoCapture(0)
    cam.set(cv.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv.CAP_PROP_FRAME_HEIGHT, height)
    cam.set(cv.CAP_PROP_FPS, 30)

    
    center = (int(height/2), int(width/2))
    radius = 100
    color = (255,255,0)
    thickness = 2

    point_1 = (0,0)
    point_2 = (int(height/2),int(width/2))

    while True:
        ret, frame = cam.read()

        cv.circle(frame, center, radius, color, thickness)
        cv.rectangle(frame, point_1, point_2, color, thickness)
        
        cv.imshow("cam", frame)

        if cv.waitKey(1) == ord('q'):
            break

    cv.DestroyAllWindows()

if __name__ == "__main__":
    #Circles()
    #Rectangles()
    #text()
    Vid()