#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from pyndamics3 import Simulation
import pandas as pd


# In[3]:


data=pd.read_csv('logistic_sample_data/logistic_sample_data_0.csv')
data


# In[4]:


t_data=data['t'].values
y_data=data['y'].values
t_data,y_data


# In[5]:


sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=1)
sim.params(r=1,K=10)
sim.run(50)


# In[7]:


plot(sim.t,sim.y)
plot(t_data,y_data,'-o')
xlabel('time')
ylabel('population')


# In[8]:


sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=1)
sim.params(r=1,K=100)
sim.run(50)

plot(sim.t,sim.y)
plot(t_data,y_data,'-o')
xlabel('time')
ylabel('population')


# In[9]:


sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=1)
sim.params(r=1,K=250)
sim.run(50)

plot(sim.t,sim.y)
plot(t_data,y_data,'-o')
xlabel('time')
ylabel('population')


# In[ ]:




