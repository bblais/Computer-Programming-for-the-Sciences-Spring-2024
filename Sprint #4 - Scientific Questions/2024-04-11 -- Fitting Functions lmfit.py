#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *

from lmfit import *


# ## Make up some data to work with

# In[ ]:


x=linspace(-10,10,20)
# ax**2+bx+c
y=4*x**2-5*x+2+randn(len(x))*50
plot(x,y,'o')


# In[ ]:


x_data,y_data = x,y


# ## Define the function
# 
# **Note:** for some odd reason, you need default values when you define the function

# In[ ]:


def quadratic_function(x, a=1, b=1, c=1):
    return a*x**2 + b*x + c


# ## Parameter exploration - check to see if our function is designed right

# In[ ]:


x=linspace(-10,10,200)
y=quadratic_function(x, a=4, b=-5, c=2)

plot(x,y)
plot(x_data,y_data,'o')


# ## Define a model in lmfit

# In[ ]:


from lmfit import Model,Parameter


# In[ ]:


quad_model=Model(quadratic_function)


# In[ ]:


quad_model.param_names


# In[ ]:


params=quad_model.make_params()
params


# ## modify any parameters as needed -- min values, max values, etc....

# In[ ]:


params['a']=Parameter("a",
                      min=0,   # minimum value
                      value=2, # initial guess
                     )


# In[ ]:


params


# ## run the fit

# In[ ]:


result=quad_model.fit(y_data,params,x=x_data)
result


# Expected:  a=4, b=-5, c=2

# ## Sometimes lmfit already has the function defined

# In[ ]:


from lmfit.models import QuadraticModel


# In[ ]:


quad_model=QuadraticModel()
result=quad_model.fit(y_data,params,x=x_data)
result


# In[ ]:


from lmfit.models import GaussianModel

gauss_model=GaussianModel()
gauss_model.param_names


# In[ ]:


df=pd.read_csv("data/peaks/sample0.csv")
df


# In[ ]:


plot(df.t,df.y,'o')


# In[ ]:


df=pd.read_csv("data/crichton/logan airport.csv")
df


# In[ ]:


t=df.YEAR
y=df.metANN

t=t.values[y<500]
y=y.values[y<500]
plot(t,y,'-o')


# In[ ]:




