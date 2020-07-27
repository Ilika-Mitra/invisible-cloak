# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:36:09 2020
@author: mitras
"""
import cv2         #opencv for image processing 
import numpy as np #numerical library for handling the image         

cap = cv2.VideoCapture(0)


# THE BACKGROUND IMAGE#
background = 0
for i in range (30):
    _,background = cap.read()
    

while (True):
    _, curent_frame = cap.read()  
    

    hsv_frame = cv2.cvtColor(curent_frame, cv2.COLOR_BGR2HSV)
    
    # blue color
    low_blue1 = np.array([90,103, 20])
    high_blue1 = np.array([119,255,255])
    blue_mask1 = cv2.inRange(hsv_frame, low_blue1, high_blue1)
    
    low_blue2 = np.array([180,98,20])
    high_blue2 = np.array([170,255,255])
    blue_mask_2= cv2.inRange(hsv_frame, low_blue2, high_blue2) 
    
    blue_mask = blue_mask_2 + blue_mask1
    
    blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations = 10) 
    blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations = 1)    
   
    
    blue_free= cv2.bitwise_not (blue_mask) # iff cloak is  not available show the present image  
    
    
    back = cv2.bitwise_and(background, background , mask = blue_mask) #substituting the blue portion (cloak part) with background image
    present = cv2.bitwise_and(curent_frame, curent_frame, mask = blue_free) #if cloak is not there show the current_frame 
    cloaked = cv2.add(back , present)
    
    cv2.imshow("CLOAKED", cloaked)
    cv2.imshow ("REAL FEED", curent_frame)
    #print("end")
    key = cv2.waitKey(1)
    
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
