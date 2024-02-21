#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from pyndamics3 import Simulation


# ## Logistic growth model
# 
# $$
# \frac{dx}{dt} = ax(1-x/K)
# $$

# In[3]:


sim=Simulation()
sim.add("x' = a*x*(1-x/K)",initial_value=2,plot=True)
sim.params(a=0.5,K=3)
sim.run(10)


# ## Free-fall model
# 
# $$
# \frac{dx}{dt} = v
# $$
# 
# $$
# \frac{dv}{dt} = -g + k v^2/m
# $$

# In[8]:


sim=Simulation()
sim.add("x' = v", initial_value=100, plot=True)
sim.add("v' = -g+k*v**2/m", initial_value=0,plot=True)
sim.params(m=1,g=9.81,k=0.1)
sim.run(6)


# In[ ]:




