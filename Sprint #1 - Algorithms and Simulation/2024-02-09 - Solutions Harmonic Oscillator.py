#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# $$
# \frac{dx}{dt}= v 
# $$
# 
# $$
# \frac{dv}{dt}= -k\cdot x/m
# $$

# ## set initial conditions for variables

# In[2]:


x=3
v=0
t=0
dt=0.01


# ## set values of parameters

# In[3]:


k=1
m=2


# ## loop the model equations
# 
# - calculate small changes in the variables
# - update variables

# In[4]:


S=Storage()

S+=t,x,v

while t<10:
    
    dx = (v) *dt  # small change in x
    dv = (-k*x/m) *dt  # small change in v
    
    x=x+dx # update the variables with small changes
    v=v+dv # update the variables with small changes
    t=t+dt
    
    S+=t,x,v  # stores the calculated values for plotting

    
t,x,v=S.arrays()


# In[5]:


plot(t,x)


# In[6]:


plot(t,v)


# In[ ]:





# ## Parameter exploration
