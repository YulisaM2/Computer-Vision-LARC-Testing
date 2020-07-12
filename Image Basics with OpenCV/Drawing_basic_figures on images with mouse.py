#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import cv2

# Functions that connect to callbacks
# The variables event, x, and y will be filled automatically depending on what happened where it was connected
# For example, x and y will be the current position of the mouse 
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image,(x,y),100,(0,0,255),-1)
    elif event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image,(x,y),100,(0,255,0),-1)

        
cv2.namedWindow('first_photo')
# This is the nexus between the main progam and the function we want to connect, reason why they are the parameters
cv2.setMouseCallback('first_photo',draw_circle)

# Now, we need top connect callback functions to add the event choice of mouse functionality
# The np.int8 makes the background screen gray, to make it black just remove the parameter
image = np.zeros((512,512,3),np.int8)

while True:
    # What is used to connect with other functions is the name of the image, so be consistent
    cv2.imshow('first_photo',image)
    if cv2.waitKey(20) & 0xFF ==27:
        break
        
cv2.destroyAllWindows()


# In[ ]:




