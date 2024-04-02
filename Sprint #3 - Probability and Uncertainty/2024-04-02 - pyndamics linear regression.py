#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *
from sci378.stats import *


# In[ ]:


data=pd.read_csv('data/dog_mass.csv')
t_data=data['days'].values[:12]
y_data=data['mass'].values[:12]

figure(figsize=(8,3))
plot(t_data, y_data, 'o')


# In[ ]:


from pyndamics3 import Simulation


# In[ ]:


# "y=mx+b"
b=1
sim=Simulation()
sim.add("y'=m",initial_value=b,plot=True)
sim.params(m=0.1)
sim.add_data(t=t_data,y=y_data,plot=True)
sim.run(220)


# In[ ]:


def logprior(m,initial_y,σ):
    value=0. 
    
    value+=logNormal(m,0,10)
    value+=logNormal(initial_y,0,10)
    value+=logJeffreys(σ)
    
    return value

def loglikelihood(sim,m,initial_y,σ):
    # pyndamics already has the data in the Simulation object
    err=sim.err(m=m,initial_y=initial_y)
    return logNormal(err,0,σ)


# In[ ]:


model=MCMCModel(sim,loglikelihood,logprior)
model.run_mcmc(400,repeat=3,verbose=True)
model.plot_chains()


# In[ ]:


model.plot_distributions()


# In[ ]:


get_ipython().run_line_magic('pinfo2', 'plot')


# In[ ]:


plot(rand(10),'-o',color='orange')
plot(rand(10),'-o',color='#34495e')


# In[ ]:




