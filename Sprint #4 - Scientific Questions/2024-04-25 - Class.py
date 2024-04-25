#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from pyndamics3 import Simulation
import pandas as pd


# In[ ]:


data=pd.read_csv('data/influenza1.csv')
data


# In[ ]:


t=array(data['Days'])
y=array(data['Patient 1'])
y = 10**y

t_data=t
y_data=y


# In[ ]:


sim=Simulation()
sim.add("T'=-β*T*V",initial_value=1e9,plot=True) # uninfected
sim.add("I'=β*T*V-δ*I",initial_value=.01,plot=True) # infected
sim.add("V'=p*I-c*V",initial_value=0,plot=True)  # viral load
sim.add_data(t=t_data,V=y_data,plot=True)
sim.params(β=3.4e-3,δ=3.4,p=7.9e-3,c=3.3) #(β=0.2,δ=0.1,p=0.5,c=0.1)
sim.run(8)


# In[ ]:


plot(sim.t,log(sim.V))
plot(t_data,log(y_data),'o')


# In[ ]:




