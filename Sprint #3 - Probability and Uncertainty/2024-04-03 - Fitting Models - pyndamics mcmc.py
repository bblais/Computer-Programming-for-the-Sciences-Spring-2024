#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *
from sci378.stats import *


# In[ ]:


data=pd.read_csv('data/growth.csv')
data


# In[ ]:


t_data=data['t'].values
y_data=data['h'].values

figure(figsize=(8,3))
plot(t_data, y_data, 'o')


# In[ ]:


from pyndamics3 import Simulation
from pyndamics3.fit import fit,Parameter


# In[ ]:


sim=Simulation()
sim.add("y'=a*y*(1-y/K)",initial_value=10,plot=True)
sim.params(a=1,K=30)
sim.add_data(t=t_data,y=y_data,plot=True)
sim.run(90)


# In[ ]:


results=fit(sim,
           Parameter("a",value=1,min=0),
           Parameter("K",value=30,min=0),
            method='powell'
           )

results


# In[ ]:





# In[ ]:


def logprior(a,K,initial_y,σ):
    value=0. 
    
    value+=logUniform(a,0,1)
    value+=logNormal(K,100,100,all_positive=True)
    value+=logNormal(initial_y,100,100,all_positive=True)
    value+=logJeffreys(σ)
    
    return value

def loglikelihood(sim,a,K,initial_y,σ):
    # pyndamics already has the data in the Simulation object
    err=sim.err(a=a,K=K,initial_y=initial_y)
    return logNormal(err,0,σ)


# In[ ]:


model=MCMCModel(sim,loglikelihood,logprior)


# In[ ]:


model.run_mcmc(300,repeat=3,verbose=True)
model.plot_chains()


# In[ ]:


model.plot_distributions()


# In[ ]:


def logprior(a,K,σ):
    value=0. 
    
    value+=logUniform(a,0,1)
    value+=logNormal(K,100,100,all_positive=True)
    value+=logJeffreys(σ)
    
    return value

def loglikelihood(sim,a,K,σ):
    # pyndamics already has the data in the Simulation object
    err=sim.err(a=a,K=K)
    return logNormal(err,0,σ)


# In[ ]:


model=MCMCModel(sim,loglikelihood,logprior)


# In[ ]:


model.run_mcmc(300,repeat=3,verbose=True)
model.plot_chains()


# In[ ]:


model.plot_distributions()


# In[ ]:




