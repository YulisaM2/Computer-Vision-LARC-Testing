#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import cv2

### Here we will try to make an algorithm that lets us draw rectangles whenever we click on the starting and ending point with the mouse
# NOTE -- Made to start from left to right (it will make weird drawings if you try and go from right to left)

# Start in false, which means the mouse is up, change to true if mouse button is down
# This will help us trigger to different events inside the draw_rectangle funtion
drawing = False

# Starting position of the mouse
# The reason why you need this variables is that we want to know from which point to which point are we drawing, which is indicated when clicking down on the mouse
sX, sY = -1,-1

# We have 3 main events: starting the rectangle, dragging and drawing the rectangle, and finishing the rectangle
# These occur when we click once, move the mouse, and release the mouse
def draw_rectangle(event,x,y,flags,params):
        
        global sX, sY, drawing
        # If the mouse was clicked down, we should start/finish drawing from the current position of the mouse
        if event==cv2.EVENT_LBUTTONDOWN:
            drawing = True
            sX,sY = x,y
        # If the mouse moves and we already clicked the mouse, it means that we should start drawing the rectangle on the area
        elif event==cv2.EVENT_MOUSEMOVE:
            if drawing==True:
                # Rectangles are continously drawn for effect (final one is on the next event)
                cv2.rectangle(image,(sX,sY),(x,y),(255,255,0),-1)
        # If the mouse was released after a click, then we should stop drawing (this helps avoid always drawing rectangles after a click by redefining drawing as false)
        elif event==cv2.EVENT_LBUTTONUP:
            drawing= False
            # Draw the final rectangle on the window
            cv2.rectangle(image,(sX,sY),(x,y),(255,255,0),-1)

            
# Creating the black image in window named photo and setting the connection between this and function draw_rectangle
image = np.zeros((512,512,3))
cv2.namedWindow('photo')
cv2.setMouseCallback('photo',draw_rectangle)

while True:
    cv2.imshow('photo',image)
    if cv2.waitKey(1) & 0xFF==27:
        break

cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




