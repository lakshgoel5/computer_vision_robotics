import cv2 as cv
import numpy as np
import sys
import tkinter as tk
from tkinter import filedialog #used for file dialog box

ftypes = [
    ("JPG", "*.jpg;*.JPG;*.JPEG"), 
    ("PNG", "*.png;*.PNG"),
    ("GIF", "*.gif;*.GIF"),
    ("All files", "*.*")
]##will show these options in file dialog box
##used to filter out and find required file


while True:


    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes = ftypes)
    root.update() #update tkinter window after file dialog closed

    image_src = cv.imread(file_path)
    cv.imshow("BGR",image_src)

    hsv=cv.cvtColor(image_src, cv.COLOR_BGR2HSV)

    #fixing variables for lower and upper values
    lowerred1=np.array([160,50,50])
    upperred1=np.array([185,255,255])
    lowerred2=np.array([0,50,50])
    upperred2=np.array([10,255,255])
    #making a mask of required region using inbuilt function
    maskred1=cv.inRange(hsv,lowerred1,upperred1)
    maskred2=cv.inRange(hsv,lowerred2, upperred2)
    #taking union of mask as red has two regions of consideration
    maskred= maskred1 | maskred2
    
    #fixing variables for lower and upper values
    lowerblue=np.array([90 ,50 ,50])
    upperblue=np.array([130 ,255 ,255])
    #making a mask of required region using inbuilt function
    maskblue=cv.inRange(hsv, lowerblue, upperblue)
    
    #building final image by taking and of mask and initial image
    resultblue = cv.bitwise_and(image_src,image_src,mask=maskblue)
    cv.imshow('resultblue',resultblue)
    resultred = cv.bitwise_and(image_src,image_src,mask=maskred)
    cv.imshow('resultred',resultred)

    #finding width to traverse from left to right
    width=image_src.shape[1]
    prevcolor="color"
    for i in range(width):
        #considering each column at a time
        pixel_maskblue = maskblue[:, i]
        #pixel_maskblue is now a 1d array of 0 and 1 of a particular column
        pixel_maskred = maskred[:,i]
        
        #The numpy.any() function tests whether any array elements along 
        #the mentioned axis evaluate to True
        if np.any(pixel_maskblue) and prevcolor != "blue":
            prevcolor="blue"
            print("Blue ",end="")
        
        elif np.any(pixel_maskred) and prevcolor != "red":
            prevcolor="red"
            print("Red ",end="")

    if(cv.waitKey(30000)==ord('q')): # wait for 30 sec and exit if q pressed.
        break

cv.destroyAllWindows()

