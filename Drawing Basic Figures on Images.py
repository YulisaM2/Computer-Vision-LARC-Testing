#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import matplotlib.pyplot as plt
import cv2 

empty= np.zeros(shape=(512,512,3), dtype= np.int16)


# In[14]:


empty.shape


# In[15]:


# Notice how as everything is colored zero from the previous function, that the image should be black
plt.imshow(empty)


# In[16]:


# To draw a rectangle use the following code
# NOTR - function will add directly into the image (won't return a new one)
# Point refer to coordinates in the image (in this case they are the crossed edges of a rectangle)
cv2.rectangle(empty, pt1 =(300,0),pt2=(410,200), color =(0,255,0), thickness= 10)


# In[17]:


#Check the new image 
plt.imshow(empty)


# In[18]:


# Trying a square in the middle of the image
cv2.rectangle(empty,pt1=(200,200),pt2=(300,300),color=(255,0,0),thickness=10)


# In[19]:


plt.imshow(empty)


# In[20]:


# Circles are mostly the same
cv2.circle(empty,(300,300),100,(0,0,255),10)


# In[21]:


plt.imshow(empty)


# In[22]:


cv2.circle(empty,(100,100),30,(100,100,100),-1)


# In[23]:


plt.imshow(empty)


# In[24]:


# To draw lines use the following (in this case it will be a diagonal line because of the coordinates inputted for pt1 and pt2)
cv2.line(empty,(0,0),(512,512),(150,250,37))


# In[25]:


plt.imshow(empty)


# In[ ]:




