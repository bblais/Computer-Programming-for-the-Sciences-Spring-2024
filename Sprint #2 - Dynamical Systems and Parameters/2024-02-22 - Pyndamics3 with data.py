#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from pyndamics3 import Simulation


# In[2]:


import pandas as pd


# In[3]:


data=pd.read_csv('data/sample_data.csv')
data


# In[5]:


t_data=data['t'].values
y_data=data['y'].values
t_data


# In[6]:


y_data


# In[8]:


plot(t_data,y_data,'o')


# In[13]:


sim=Simulation()
sim.add("y'=a*y*(1-y/K)",initial_value=2,plot=True)
sim.params(a=0.1,K=10)
sim.run(50)


# In[14]:


sim=Simulation()
sim.add("y'=a*y*(1-y/K)",initial_value=2,plot=True)
sim.params(a=0.1,K=10)
sim.add_data(t=t_data,y=y_data,plot=True)
sim.run(50)


# In[18]:


sim=Simulation()
sim.add("y'=a*y*(1-y/K)",initial_value=2,plot=True)
sim.params(a=1,K=400)
sim.add_data(t=t_data,y=y_data,plot=True)
sim.run(50)


# In[19]:


sim=Simulation()
sim.add("y'=a*y*(1-y/K)",initial_value=2,plot=True)
sim.add("x'=2*a*x*(1-x/(K*1.3))",initial_value=5,plot=True)
sim.params(a=1,K=400)
sim.add_data(t=t_data,y=y_data,plot=True)
sim.run(50)


# Quick and dirty way of plotting two simulations

# In[20]:


sim=Simulation()
sim.add("y'=a*y*(1-y/K)",initial_value=2,plot=1)
sim.add("x'=2*a*x*(1-x/(K*1.3))",initial_value=5,plot=1)
sim.params(a=1,K=400)
sim.add_data(t=t_data,y=y_data,plot=True)
sim.run(50)


# Better way -- turn off plot=True, and plot manually

# In[21]:


sim=Simulation()
sim.add("y'=a*y*(1-y/K)",initial_value=2,plot=False)
sim.add("x'=2*a*x*(1-x/(K*1.3))",initial_value=5,plot=False)
sim.params(a=1,K=400)
sim.add_data(t=t_data,y=y_data,plot=True)
sim.run(50)


# In[25]:


plot(sim.t,sim.y,'b-')
plot(t_data,y_data,'bo')
plot(sim.t,sim.x,'r-')


# In[ ]:




