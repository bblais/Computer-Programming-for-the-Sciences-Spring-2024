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


# In[10]:


sim=Simulation()
sim.add("p' = r*p*(1-p/K)",initial_value=1)
sim.params(r=1,K=250)
sim.run(50)

plot(sim.t,sim.y)
plot(t_data,y_data,'-o')
xlabel('time')
ylabel('population')


# $$
# \frac{dy}{dt}=ry(1-y/K)
# $$

# In[11]:


sim=Simulation()
sim.add("p' = r*p*(1-p/K)",initial_value=1)
sim.params(r=1,K=250)
sim.run(50)

plot(sim.t,sim.p)
plot(t_data,y_data,'-o')
xlabel('time')
ylabel('population')


# In[13]:


sim=Simulation()
sim.add("p' = r*p*(1-p/K)",initial_value=1,plot=True)
sim.params(r=1,K=250)
sim.add_data(t=t_data,p=y_data,plot=True)
sim.run(50)


# In[ ]:




