#!/usr/bin/env python
# coding: utf-8

# In[13]:


import cv2
import matplotlib.pyplot as plt

# Default will be BRG
image = cv2.imread('PhotosLARC/horizontal.png')


# In[14]:


plt.imshow(image)


# In[15]:


# Changing it from BGR to RGB
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image)


# In[18]:


# Changing it from RGB to HSV
image = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
plt.imshow(image)

image = cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
# Changing it from RGB to HSL
image = cv2.cvtColor(image,cv2.COLOR_RGB2HLS)
plt.imshow(image)


# In[ ]:




