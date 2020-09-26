#Generating the certificates

import cv2  
import numpy as np  
import os
import csv
import xlrd   


loc = ("data.xlsx")  

f1 = open("coordinates.txt","r")
coordinates = f1.read().split("\n")
 
flag=True

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
  
for i in range(sheet.nrows): 
    name=sheet.cell_value(i, 0)
    date=sheet.cell_value(i, 1)
    signature =sheet.cell_value(i, 2)

    # Load image in OpenCV  
    img = cv2.imread("sample.jpg")  

    #select the font for the generated certificates 
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Draw the text 

    img=cv2.putText(img, name, (int(coordinates[0]),int(coordinates[1])+15),font,1,(0,0,255),2)
    img=cv2.putText(img, date, (int(coordinates[2]),int(coordinates[3])+15),font,1,(255,0,0),2)
    img=cv2.putText(img, signature, (int(coordinates[4]),int(coordinates[5])+15),font,1,(0,255,0),2)
    
    if flag:
        cv2.imshow('Certificate', img) 
        flag=False
        
    path = ''
    cv2.imwrite('./Generated_Certificates/'+name+'.png',img)
    
    cv2.waitKey(0)  

    cv2.destroyAllWindows()
    
    



