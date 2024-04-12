#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *
from lmfit import *


# ## Novick-Weiner Data

# In[ ]:


data=pd.read_csv('data/g149novickA.txt',header=None)
data.head()


# In[ ]:


t=data[0]
z=data[1]
plot(t,z,'-o')


# In[ ]:


from pyndamics3 import Simulation
from pyndamics3.fit import fit,Parameter


# $$
# \frac{dz}{dt}= \frac{S}{\tau}-\frac{z}{\tau}
# $$

# In[ ]:


sim=Simulation()
sim.add("z'=S/τ-z/τ",0,plot=True)
sim.params(S=1,τ=2)
sim.add_data(t=t,z=z,plot=True)
sim.run(7)


# In[ ]:


result=fit(sim,
          Parameter("S",value=1,min=0),
          Parameter("τ",value=1,min=0))
result


# In[ ]:


sim.run(7)


# In[ ]:


plot(t,z,'o')
plot(sim.t,sim.z)


# In[ ]:




