#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378.stats import *


# In[ ]:


def logprior(μ):
    value=0
    
    value+=logNormal(μ,0,100)
    
    return value

def loglikelihood(data,μ):
    x=data
    
    value=0
    σ=2
        
    value+=logNormal(x-μ,0,σ)
    return value
    


# In[ ]:





# In[ ]:





# In[ ]:


drug = (101,100,102,104,102,97,105,105,98,101,100,123,105,103,100,95,102,106,
        109,102,82,102,100,102,102,101,102,102,103,103,97,97,103,101,97,104,
        96,103,124,101,101,100,101,101,104,100,101)
placebo = (99,101,100,101,102,100,97,101,104,101,102,102,100,105,88,101,100,
           104,100,100,100,101,102,103,97,101,101,100,101,99,101,100,100,
           101,100,99,101,100,102,99,100,99)


# In[ ]:


x=drug
model=MCMCModel(x,loglikelihood,logprior,
               μ=Normal(10,10))   # initial guess for μ


# In[ ]:


model.run_mcmc(400,repeat=3,verbose=True)
model.plot_chains()


# In[ ]:


model.plot_distributions()


# In[ ]:


model.P("μ>101.5")


# In[ ]:




