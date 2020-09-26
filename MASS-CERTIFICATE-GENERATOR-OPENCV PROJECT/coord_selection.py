
# Capturing mouse clicks

import cv2 as cv
import numpy as np

f = open("coordinates.txt","w")

# mouse callback function

def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.putText(img,"Coordinates (%d,%d)"%(x,y),(80,60),3,1,(0,0,255)) 
        f.write(str(x)+"\n")                                           
        f.write(str(y)+"\n")    

img = cv.imread("sample.jpg")                                         
                                                                          
cv.namedWindow('SELECTION')
cv.setMouseCallback('SELECTION',draw_circle)
while(1):
    cv.imshow('SELECTION',img)
    if cv.waitKey(10) & 0xFF == 27:   #Escape Key to terminate window
        break

cv.destroyAllWindows()   

f.close()