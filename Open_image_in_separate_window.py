#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

# To open the image in a separate window use the following code
# Note that the image is openning in original size so it might be too big for your screen!
image = cv2.imread('LARCVision/PhotosLARC/horizontal.png')
while True:
    cv2.imshow('STACKS',image)
    # Wait 1 millisecond and if the key 'escape' was pressed break;
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()


# In[ ]:




