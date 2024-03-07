#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from pyndamics3 import Simulation
import pandas as pd


# In[19]:


data=pd.read_csv('logistic_sample_data/logistic_sample_data_2.csv')
t_data=data['t'].values
y_data=data['y'].values/8
plot(t_data,y_data,'o')


# In[27]:


r=.4
sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=1)
sim.params(r=r,K=50)
sim.run(50)

plot(sim.t,sim.y,linewidth=3)
plot(t_data,y_data,'o')
xlabel('time')
ylabel('population')


sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=0)  # first fixed point
sim.params(r=r,K=50)
sim.run(50)
plot(sim.t,sim.y,'r--')

text(10,1,'Fixed point #1: $y=0$')

sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=50)  # second fixed point
sim.params(r=r,K=50)
sim.run(50)
plot(sim.t,sim.y,'g--')
text(10,46,'Fixed point #2: $y=K$')

sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=53)  # above second fixed point 
sim.params(r=r,K=50)
sim.run(50)
plot(sim.t,sim.y,'g:')

sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=47)  # below second fixed point 
sim.params(r=r,K=50)
sim.run(50)
plot(sim.t,sim.y,'g:')

sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=3)  # above first fixed point 
sim.params(r=r,K=50)
sim.run(50)
plot(sim.t,sim.y,'r:')

sim=Simulation()
sim.add("y' = r*y*(1-y/K)",initial_value=-3)  # below first fixed point 
sim.params(r=r,K=50)
sim.run(4)
plot(sim.t,sim.y,'r:')

text(3,51,'Stable fixed point #2',fontsize=10,weight='bold',color='g')
text(3,-5,'Unstable fixed point #1',fontsize=10,weight='bold',color='r')


# In[ ]:




