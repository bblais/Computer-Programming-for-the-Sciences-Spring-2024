#!/usr/bin/env python
# coding: utf-8

# ## Simulation
# 
# 1. set the parameters (e.g. a=0.0083)
# 2. set the initial value for variables (e.g. p=7e9)
# 3. set the simulation parameters (e.g. dt=0.1)
# 4. set t=0
# 5. loop
#    1. apply model equations  (e.g. dp/dt=a*p  -->  dp=a*p*dt)
#    2. update the variables and time (e.g. p=p+dp;  t=t+dt)

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
# make the plots appear in the notebook
from pylab import *  # be lazy about importing all the math and plotting functions
from sci378 import *  # be lazy about all the functions for the class


# ## Set the parameters

# In[2]:


a=0.0083


# ## Set the initial variables

# In[3]:


p=7e9


# ## Set the simulation parameters

# In[4]:


dt=0.1


# ## Set initial time

# In[5]:


t=0


# In[6]:


S=Storage()  # set up a storage to keep track of the calculations

S+=t,p  #  add the starting values to the storage
while t<10:

    # apply the model equations
    dp=a*p   # small change in p

    # update the variables and time
    p=p+dp
    t=t+dt

    S+=t,p  #  add the updated values to the storage

t,p=S.arrays()  # get the stored values as arrays so we can plot, etc...


# In[7]:


plot(t,p)


# In[ ]:




