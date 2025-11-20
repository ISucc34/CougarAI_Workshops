import cv2 as cv

image = "test.jpeg"

def imageShow():
    matrix = cv.imread(image)#Reading turns it into a matrix
    cv.imshow("cat", matrix) 

    cv.waitKey(0) #Waits for keypress in miliseconds, 0 means wait indefinitely, 
    cv.DestroyAllWindows()



if __name__ == "__main__":
    imageShow()
    
