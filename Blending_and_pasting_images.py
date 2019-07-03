#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import cv2

# Remeber that default conversion is BGR not RGB
# image1 and image2 have the same size, but not image3
image1= cv2.imread('PhotosLARC/horizontal.png')
image2= cv2.imread('PhotosLARC/oneHalfHorizontal.png')

image1= cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
image2= cv2.cvtColor(image2,cv2.COLOR_BGR2RGB)

image3= image1.copy()

plt.imshow(image1)


# In[3]:


plt.imshow(image2)


# In[4]:


image1.shape


# In[5]:


image2.shape


# In[6]:


# This images are of the same size, reason why we do not need to use masks to resize them (in case that they had different dimensions, we would have to do that)
# Blend images usinf addWeighted function with your selection of importance per image
blend = cv2.addWeighted(image1,0.6,image2,0.4,0)
plt.imshow(blend)


# In[7]:


# Now let's try overlay a smaller image on top of a larger one without blending
# We can use numpy reassignment 


# In[ ]:





# In[8]:


# Notice both have the same dimensions
image1.shape


# In[9]:


image2.shape


# In[10]:


# Using resize we will make image2 even smaller so that we have a difference in size
image2 = cv2.resize(image2,(1000,1500))
image2.shape


# In[11]:


# We need to know from where are we going to start and end our image overlay (we will start on top left corner) 
sX, sY = 0,0
# end is equal to start + size (for x we need the width and for y the height) 
eX, eY = sX + image2.shape[1], sY + image2.shape[0] 

# Overlaying is about replacing a certain chunck of pixels with other ones so we are going to reassing the values of the numpy array of the bigger image with all of the ones located in the smaller one
# Be careful! how images store dimensions is different of how numpy arrays store them (HW vs WH)
image1[sY:eY,sX:eX] = image2

plt.imshow(image1)


# In[12]:


# Now,let's blend images of different sizes (for blending we can not use addWeighted)
# First decide where we want to blend (our region of interest or ROI), which in this case will be the right and down corner
# We will use image3 which is a copy of image1 for this exercise
image3.shape
sX,sY = 4032 - image2.shape[1], 1960 - image2.shape[0]

# Now we need to create save the ROI
rows,cols,channels = image2.shape


# In[13]:


roi = image1[sY:1960,sX:4032]


# In[14]:


# Let's see if our ROI has been alocated correctly
plt.imshow(roi)


# ###### 

# In[15]:


# Now we have to make a mask to only grab certain colors
# We need to get in pure white the parts of the image2 we want to actually put into image1
# Using gray scale we can see where most of the color is, so we need to inverse it so that the concentration in black can become white for our purposes


# In[16]:


image2gray = cv2.cvtColor(image2,cv2.COLOR_RGB2GRAY)


# In[17]:


plt.imshow(image2gray,'gray')


# In[18]:


mask_inverse = cv2.bitwise_not(image2gray)
plt.imshow(mask_inverse)


# In[19]:


# See how we have inverted it? Now white is color, and black is its absence
plt.imshow(mask_inverse,'gray')


# In[28]:


# Add the color channels 
mask_inverse.shape
mask_inverse


# In[29]:


white_background = np.full(image2.shape,255,np.uint8)
white_background.shape


# In[30]:


# Calculate disjunction of 2 arrays
# We will use it to make sure that we have selected the white part in all 3 of the color channels
background = cv2.bitwise_or(white_background,white_background,mask_inverse)


# In[31]:


background.shape


# In[32]:


plt.imshow(background)


# In[33]:


# Adding the mask to original image 
foreground = cv2.bitwise_or(image2,image2,mask_inverse)


# In[34]:


plt.imshow(foreground)


# In[36]:


# Add the edited image on image3 (our base where our ROI is)
final_roi = cv2.bitwise_or(roi,foreground)


# In[37]:


plt.imshow(final_roi)


# In[ ]:


# Finally, reconstruct the final image created by image3 + image2 with mask


# In[41]:


image3[sY:sY + final_roi.shape[0],sX:sX + final_roi.shape[1]] = final_roi


# In[42]:


plt.imshow(image3)


# In[ ]:




