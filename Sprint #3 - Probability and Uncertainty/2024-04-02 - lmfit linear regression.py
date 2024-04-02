#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *
from sci378.stats import *


# In[ ]:


from lmfit import Model,Parameter


# In[ ]:


data=pd.read_csv('data/dog_mass.csv')
t_data=data['days'].values[:12]
y_data=data['mass'].values[:12]

figure(figsize=(8,3))
plot(t_data, y_data, 'o')


# In[ ]:


def linear(x,m=1,b=1):
    return m*x+b


# In[ ]:


mymodel=linear_model=Model(linear)  # from lmfit  # make sure to call it mymodel
params=mymodel.make_params()
params['m']=Parameter("m",min=0,value=0.5)
params


# In[ ]:


result=mymodel.fit(y_data,params,x=t_data)
result


# In[ ]:




