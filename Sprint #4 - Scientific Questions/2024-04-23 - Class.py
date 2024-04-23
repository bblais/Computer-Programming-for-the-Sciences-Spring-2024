#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[ ]:


y=array([.5,3,2,4.1,.7])  # this is logged data
y=10**y

t=array([0,1,2,3,4])


# In[ ]:


figure(figsize=(6,3))
plot(t,y,'-o')


# In[ ]:


figure(figsize=(6,3))
plot(t,y,'-o')
yscale('log')


# In[ ]:




