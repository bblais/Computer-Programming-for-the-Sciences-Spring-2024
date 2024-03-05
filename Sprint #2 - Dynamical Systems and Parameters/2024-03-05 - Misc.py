#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from pyndamics3 import Simulation


# In[15]:


sim=Simulation()
sim.figsize=(6,3)
sim.add("y'=a",1,plot=True)
sim.params(a=2)
sim.run(10)


# Let's say the constant changes midway

# In[16]:


def a(t,t1):
    if t<t1:
        return 2
    else:
        return 4


sim=Simulation()
sim.figsize=(6,3)
sim.add("y'=a(t,t1)",1,plot=True)
sim.params(t1=5)
sim.functions(a)
sim.run(10)


# In[17]:


import pandas as pd


# In[ ]:




