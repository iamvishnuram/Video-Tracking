import numpy as n
import cv2 as cv

video = cv.VideoCapture(0)

while (1):
    _,frame = video.read()
    
    new_image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    #cv.imshow('hsvimage', new_image)

    lower = n.array([0,100,100])
    upper = n.array([20,255,255])
    mask = cv.inRange(new_image, lower, upper)
   # cv.imshow('mask', mask)

    result = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('result', result)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()