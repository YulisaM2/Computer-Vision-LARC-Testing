#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

from PIL import Image

#First we need to extract from its address the image that we are going to use
photo = Image.open('LARCVision/PhotosLARC/horizontal.png')


# In[8]:


photo


# In[23]:


# Here we can see that this variable contains a reference to an image of type PNG
type(photo)


# In[10]:


#However, that is not valuable for our computers, they need the data in form of arrarys, so we need to transform it into an array
pic_arr = np.asarray(photo)


# In[11]:


# Here we can see how photo is still a PNG while pic_arr is a nparray
type(photo)


# In[12]:


type(pic_arr)


# In[13]:


# Shape gives us the Height X Width X Color channels of an image (default is RGB, reason why channels = 3) 
pic_arr.shape


# In[24]:


plt.imshow(pic_arr)


# In[25]:


pic_red = pic_arr.copy()


# In[ ]:





# In[ ]:


# If we only want to display all the elements from one channel we can do the following


# In[26]:


plt.imshow(pic_red[:,:,0])


# In[19]:


# Remember that the default scale is not RGB when using imshow, reason why the previous image is yellowish 
# First channel is Red, then Green and finally Blue
plt.imshow(pic_red[:,:,0],"gray")


# In[20]:


plt.imshow(pic_red[:,:,1],"gray")


# In[21]:


plt.imshow(pic_red[:,:,2],"gray")


# In[27]:


# Remember that this follows a 0 to 255 scale, the closest the number is to 0 (whitest) the strongest the color is in that area


# In[ ]:




