#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from pyndamics3 import Simulation


# ![image.png](attachment:ec74a94b-0871-4b00-a0fa-ee16cf4c39b1.png)
# 
# ![image.png](attachment:de8b16cf-b017-4a7a-8834-9342b651fb77.png)

# In[2]:


sim=Simulation()
sim.add(" x' = α*x - β*x*y",10,plot=True)
sim.add(" y' = δ*x*y-γ*y",10,plot=True)
sim.params(α=1.1 ,β=0.4, δ=.1, γ=.4 )
sim.run(100)


# In[3]:


sim=Simulation()
sim.add(" x' = α*x - β*x*y",4.1)
sim.add(" y' = δ*x*y-γ*y",3)
sim.params(α=1.1 ,β=0.4, δ=.1, γ=.4 )
sim.run(100)

figure(figsize=(8,4))
plot(sim.t,sim.x)
plot(sim.t,sim.y)

plot(sim.t,0*ones(len(sim.t)),'r--')

# prey
plot(sim.t,(.4/.1)*ones(len(sim.t)),'c--')

# predator
plot(sim.t,(1.1/.4)*ones(len(sim.t)),'r--')


# In[4]:


sim=Simulation()
sim.add(" x' = α*x - β*x*y",4.1)
sim.add(" y' = δ*x*y-γ*y",3)
sim.params(α=1.1 ,β=0.4, δ=.1, γ=.4 )
sim.run(100)

figure(figsize=(8,4))
plot(sim.t,sim.x)
plot(sim.t,sim.y)

plot(sim.t,0*ones(len(sim.t)),'r--')

# prey
plot(sim.t,(sim.γ/sim.δ)*ones(len(sim.t)),'c--')

# predator
plot(sim.t,(1.1/.4)*ones(len(sim.t)),'r--')


# In[5]:


γ=.4
δ=.1


sim=Simulation()
sim.add(" x' = α*x - β*x*y",γ/δ+.1)
sim.add(" y' = δ*x*y-γ*y",3)
sim.params(α=1.1 ,β=0.4, δ=δ, γ=γ )
sim.run(100)

figure(figsize=(8,4))
plot(sim.t,sim.x)
plot(sim.t,sim.y)

plot(sim.t,0*ones(len(sim.t)),'r--')

# prey
plot(sim.t,(sim.γ/sim.δ)*ones(len(sim.t)),'c--')

# predator
plot(sim.t,(1.1/.4)*ones(len(sim.t)),'r--')


# In[ ]:





# In[6]:


plot(sim.x,sim.y)
axis('equal')


# In[7]:


sim=Simulation()
sim.add(" x' = α*x - β*x*y",10,plot=1)
sim.add(" y' = δ*x*y-γ*y",10,plot=1)
sim.params(α=1.1 ,β=0.4, δ=.1, γ=.4 )
sim.run(100)


# ## Not needed for the solution but cool anyway

# In[8]:


import pyndamics3


# In[9]:


pyndamics3.phase_plot(sim,'x','y')
plot([0],[0],'ro')
plot([sim.γ/sim.δ],[sim.α/sim.β],'ro')


# In[10]:


pyndamics3.vector_field(sim,rescale=True,x=linspace(0,30,20),y=linspace(0,15,20))


# In[ ]:




