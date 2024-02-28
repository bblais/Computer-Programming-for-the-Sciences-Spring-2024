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


# ## Fixed point plot for logistic growth

# In[24]:


sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=1)
sim.params(r=1,K=50)
sim.run(50)

plot(sim.t,sim.y,linewidth=3)
xlabel('time')
ylabel('population')


sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=0)  # first fixed point
sim.params(r=1,K=50)
sim.run(50)
plot(sim.t,sim.y,'--')

text(10,1,'Fixed point #1: $y=0$')

sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=50)  # second fixed point
sim.params(r=1,K=50)
sim.run(50)
plot(sim.t,sim.y,'--')
text(10,46,'Fixed point #2: $y=K$')


# In[40]:


sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=1)
sim.params(r=1,K=50)
sim.run(30)

plot(sim.t,sim.y,linewidth=3)
xlabel('time')
ylabel('population')


sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=0)  # first fixed point
sim.params(r=1,K=50)
sim.run(30)
plot(sim.t,sim.y,'r--')

text(10,1,'Fixed point #1: $y=0$')

sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=50)  # second fixed point
sim.params(r=1,K=50)
sim.run(30)
plot(sim.t,sim.y,'g--')
text(10,46,'Fixed point #2: $y=K$')

sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=53)  # above second fixed point 
sim.params(r=1,K=50)
sim.run(30)
plot(sim.t,sim.y,'g:')

sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=47)  # below second fixed point 
sim.params(r=1,K=50)
sim.run(30)
plot(sim.t,sim.y,'g:')

sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=3)  # above first fixed point 
sim.params(r=1,K=50)
sim.run(30)
plot(sim.t,sim.y,'r:')

sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=-3)  # below first fixed point 
sim.params(r=1,K=50)
sim.run(2)
plot(sim.t,sim.y,'r:')

text(1,51,'Stable fixed point #2',fontsize=10,weight='bold',color='g')
text(1,-5,'Unstable fixed point #1',fontsize=10,weight='bold',color='r')


# In[ ]:




