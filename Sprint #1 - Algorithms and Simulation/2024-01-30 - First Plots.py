#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[2]:


a=linspace(-5,5,21)
a


# In[3]:


a=linspace(-5,5,27)
a


# In[5]:


a=linspace(-5,5,21)
2*a


# In[7]:


x=linspace(-5,5,21)
y=2*x-3
plot(x,y)

y=2*x**2-2*x+3
plot(x,y)


# In[9]:


x=linspace(-5,5,11)
y=2*x-3
plot(x,y,'-o')

y=2*x**2-2*x+3
plot(x,y,'-x')


# In[ ]:




