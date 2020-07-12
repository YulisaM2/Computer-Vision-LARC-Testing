#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# This will create an np array with ints going 2 by 2 from 0 to 9
np.arange(0,10,2)


# In[2]:


# This is basically to create a matrix of n x m filled with 0s
np.zeros(shape=(10,5))


# In[4]:


# Same as .zeros but with 1s
np.ones(shape=(3,2))


# In[10]:


# Using random.seed and random.randint will let us create a specific selection of random numbers
# In other words, a known random array (in this case 10 elements from 1 to 99)
np.random.seed(101)
arr = np.random.randint(0,100,10)
arr


# In[11]:


arr2 = np.random.randint(0,100,10)


# In[12]:


arr2


# In[13]:


# Shape is used to get the size of the array
arr.shape


# In[14]:


# Reshape allows us to reorganize an array while the selected dimensions respect the amount of elements inside of it
arr.reshape((2,5))


# In[15]:


arr3 = np.arange(0,10).reshape((2,5))


# In[16]:


arr3


# In[17]:


arr3.reshape((1,10))


# In[18]:


arr3.shape


# In[19]:


arr3.reshape((2,5))


# In[20]:


arr3[1][3]


# In[21]:


arr3[1,3]


# In[22]:


# To get the elements located in col = 1
arr3[:,1]


# In[23]:


# To get the elements located in row = 1
arr3[1,:]


# In[27]:


# To acces just a chunck of the actual matrix (from row 0 to 1 and column from 0 to 4)
arr3[0:2,0:5]


# In[28]:


# Which is in this case the same as 
arr3[:,:]


# In[ ]:




