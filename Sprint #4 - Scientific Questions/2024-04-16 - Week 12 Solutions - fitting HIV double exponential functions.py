#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[ ]:


from sci378 import *


# In[ ]:


from lmfit import *


# See: https://lmfit.github.io/lmfit-py/builtin_models.html  for more examples

# ## HIV
# 

# In[ ]:


data=pd.read_csv("data/HIVseries.csv",header=None)
data


# In[ ]:


x=data[0]
y=data[1]


# In[ ]:


plot(x,y,'o')


# ## Step 1 - define the function

# In[ ]:


def double_exponential(t,A=1,α=.1,B=1,β=1):
    return A*exp(-α*t)+ B*exp(-β*t)


# ## Step 1a - parameter exploration

# In[ ]:


tt=linspace(0,7,100)
VV=double_exponential(tt,A=120000,α=.2,B=60000,β=2.5)

plot(x,y,'o')
plot(tt,VV,'-')


# ## Step 2 - define the model and construct the parameter list

# In[ ]:


mymodel=Model(double_exponential)   # from lmfit


# In[ ]:


mymodel.param_names


# In[ ]:


params=mymodel.make_params()
params


# ## Step 3 - modify the parameter list (min, max, etc...) as needed

# In[ ]:


params['A']=Parameter("A",min=1000,value=120000,vary=False)
params['B']=Parameter("B",min=1000,value=60000,vary=False)
params['α']=Parameter("α",min=0,value=1)
params['β']=Parameter("β",min=0,value=1)
params


# ## Step 4 - do the fit, look at the parameter values (do they make sense?), etc...

# In[ ]:


result = mymodel.fit(y, params, t=x)
result


# ## Step 5 - plot your data and the predictions of the model

# In[ ]:


plot(x,y,'o')

tt=linspace(0,7,100)
VV=result.eval(t=tt)

plot(tt,VV,'-')



# In[ ]:




