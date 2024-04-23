#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[ ]:


y=array([.5,3,2,4.1,.7])  # this is logged data
y=10**y

t=array([0,1,2,3,4])
t_data=t
y_data=y


# In[ ]:


figure(figsize=(6,3))
plot(t,y,'-o')


# In[ ]:


figure(figsize=(6,3))
plot(t,y,'-o')
yscale('log')


# In[ ]:


from pyndamics3 import Simulation


# In[ ]:


sim=Simulation()
sim.add("T'=-β*T*V",initial_value=1,plot=True)
sim.add("I'=β*T*V-δ*I",initial_value=1,plot=True)
sim.add("V'=p*I-c*V",initial_value=1,plot=True)
sim.add_data(t=t_data,V=log(y_data),plot=True)
sim.params(β=0.2,δ=0.1,p=0.5,c=0.1)
sim.run(7)


# In[ ]:




