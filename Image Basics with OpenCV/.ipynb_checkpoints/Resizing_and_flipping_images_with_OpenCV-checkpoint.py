#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import cv2


# In[16]:


# Skip saving as np and then trasnforming into array by using this
# Be careful because if the path is broken it will not tell you (prone to mistakes)
image = cv2.imread('../PhotosLARC/horizontal.png')


# In[17]:


type(image)


# In[18]:


image.shape


# In[19]:


# For OpenCV the order of RGB channels are actually Blue Green Red (matplotlib uses standard RGB)
# Hence, we need to transform it using cvtColor
newImage = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


# In[20]:


plt.imshow(newImage)


# In[21]:


# You can also convert it directly from one scale to another using imread (will only include the channels needed by the new scale)
greyImage = cv2.imread('../PhotosLARC/horizontal.png', cv2.IMREAD_GRAYSCALE)


# In[22]:


greyImage.shape


# In[23]:


plt.imshow(greyImage, "gray")


# In[24]:


# To resize image use resize function whose order for new dimensions uses Width X Height format (be careful!)
# Can use hard coded values or ratios (resize(image,(0,0), image, widthRatio, heigthRatio))
newImage.shape


# In[25]:


resizedImage = cv2.resize(newImage,(200,400))
plt.imshow(resizedImage)


# In[12]:


# New values for the resized image
resizedImage.shape


# In[ ]:


# In order to flip an image just use cv2.flip function
# 0 for vertical flip and 1 for horizontal flip and -1 for both


# In[33]:


resizedImage = cv2.flip(newImage,-1)
plt.imshow(resizedImage)


# In[35]:


# To create a new file we need to write an nparray using imwrite
# We create a new directory based on the image used
cv2.imwrite('rotatedImage.jpg',resizedImage)


# In[40]:


# NOTE -- TO CHANGE HOW MUCH CANVA'S SPACE IN NOTEBOOK TO USE, ADD THE FOLLOWING CODE
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.imshow(resizedImage)


# In[ ]:




