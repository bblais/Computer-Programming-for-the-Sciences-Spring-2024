#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *
from sci378.stats import *


# In[ ]:


data=pd.read_csv('data/dog_mass.csv')
t_data=data['days'].values
y_data=data['mass'].values

figure(figsize=(8,3))
plot(t_data, y_data, 'o')


# In[ ]:


from pyndamics3 import Simulation


# In[ ]:


sim=Simulation()
sim.add("y'=a*y*(1-y/K)",initial_value=1,plot=True)
sim.params(a=0.1,K=100)
sim.add_data(t=t_data,y=y_data,plot=True)
sim.run(1250)


# In[ ]:


def logprior(a,K,initial_y,σ):
    value=0. 
    
    value+=logUniform(a,0,1)
    value+=logUniform(K,0,200)
    value+=logUniform(initial_y,0,10)
    value+=logJeffreys(σ)
    
    return value

def loglikelihood(sim,a,K,initial_y,σ):
    # pyndamics already has the data in the Simulation object
    err=sim.err(a=a,K=K,initial_y=initial_y)
    return logNormal(err,0,σ)


# In[ ]:


model=MCMCModel(sim,loglikelihood,logprior)


# In[ ]:


model.run_mcmc(400,repeat=3,verbose=True)
model.plot_chains()


# In[ ]:


model.plot_distributions()


# In[ ]:


from pyndamics3.fit import fit,Parameter


# In[ ]:


results=fit(sim,
           Parameter("a",value=1,min=0),
           Parameter("K",value=150,min=0),
           Parameter("initial_y",value=1),
           )


# In[ ]:


sim.data_components


# In[ ]:




