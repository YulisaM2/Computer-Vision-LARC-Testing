#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import cv2 

empty= np.zeros(shape=(512,512,3), dtype= np.int16)


# In[2]:


empty.shape


# In[3]:


# Notice how as everything is colored zero from the previous function, that the image should be black
plt.imshow(empty)


# In[4]:


# To draw a rectangle use the following code
# NOTR - function will add directly into the image (won't return a new one)
# Point refer to coordinates in the image (in this case they are the crossed edges of a rectangle)
cv2.rectangle(empty, pt1 =(300,0),pt2=(410,200), color =(0,255,0), thickness= 10)


# In[5]:


#Check the new image 
plt.imshow(empty)


# In[6]:


# Trying a square in the middle of the image
cv2.rectangle(empty,pt1=(200,200),pt2=(300,300),color=(255,0,0),thickness=10)


# In[7]:


plt.imshow(empty)


# In[8]:


# Circles are mostly the same
cv2.circle(empty,(300,300),100,(0,0,255),10)


# In[9]:


plt.imshow(empty)


# In[10]:


cv2.circle(empty,(100,100),30,(100,100,100),-1)


# In[11]:


plt.imshow(empty)


# In[12]:


# To draw lines use the following (in this case it will be a diagonal line because of the coordinates inputted for pt1 and pt2)
cv2.line(empty,(0,0),(512,512),(150,250,37))


# In[13]:


plt.imshow(empty)


# In[14]:


# To write in an image, use the fonts supported by cv2 library
# To put it into text use the following function
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(empty,'Testing',(300,500),font,1,(255,255,255),5,cv2.LINE_AA)
plt.imshow(empty)


# In[15]:


# To draw personalized polygons do the following
empty = np.zeros((512,512,3),np.int32)
plt.imshow(empty)


# In[16]:


# First, organize the vertices of the figure
vertices = np.array([[100,300],[200,200],[400,300],[200,400]],np.int32)


# In[18]:


vertices
vertices.shape


# In[20]:


# Then, cast them into 3 dimension for the 3 channels of RGB or you'll get an error
pts = vertices.reshape((-1,1,2))
pts.shape


# In[25]:


# This will create the figure, notive==ce that by format you need to pass your vertices as a list
cv2.polylines(empty,[pts],isClosed = True,color=(255,0,0), thickness=4)
plt.imshow(empty)


# In[ ]:




