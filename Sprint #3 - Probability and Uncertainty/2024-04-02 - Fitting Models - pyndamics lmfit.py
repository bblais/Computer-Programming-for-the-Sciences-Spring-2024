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


from pyndamics3.fit import fit,Parameter


# In[ ]:


results=fit(sim,
           Parameter("a",value=1,min=0,max=1),
           Parameter("K",value=150,min=0,max=200),
           Parameter("initial_y",value=1,min=0),
           )


# In[ ]:


results


# In[ ]:




