
#################################################
######### Capturing Mouse Clicks#################
#################################################


import cv2 as cv
import numpy as np

f = open("coordinates.txt","w")

# mouse callback function
#Function to select required coordinates and saving them in the folder 

def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.putText(img,"Coordinates (%d,%d)"%(x,y),(80,60),3,1,(0,0,255)) 
        f.write(str(x)+"\n")                                           
        f.write(str(y)+"\n")   

# Load image in OpenCV 
#  
img = cv.imread("sample.jpg")                                         

 #Creating a new window                                                                       
cv.namedWindow('SELECTION')
cv.setMouseCallback('SELECTION',draw_circle)

while(1):
    cv.imshow('SELECTION',img)
    if cv.waitKey(10) & 0xFF == 27:   #Escape Key to terminate window
        break

cv.destroyAllWindows()   

f.close()
