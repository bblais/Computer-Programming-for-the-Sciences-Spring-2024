#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[2]:


# y=a*sin^2(θ)


# In[7]:


S=Storage()

θ=0
dθ=0.1
a=1

while θ<180:

    y=a*sin(radians(θ))**2
    S+=θ,y

    θ=θ+dθ

θ,y=S.arrays()
plot(θ,y)


# In[9]:


for a in [1,2,3,4]:
    S=Storage()
    
    θ=0
    dθ=0.1
    #a=1
    
    while θ<180:
    
        y=a*sin(radians(θ))**2
        S+=θ,y
    
        θ=θ+dθ
    
    θ,y=S.arrays()
    plot(θ,y)X


# In[11]:


for a in [1,2,3,4]:
    θ=linspace(0,180,400)
    y=a*sin(radians(θ))**2
    plot(θ,y)


# In[12]:


alpha=5


# In[ ]:


α


# In[13]:


# \theta  # hit tab

θ=5


# In[ ]:




