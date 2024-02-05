#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[2]:


def f(x):
    # f(x)=4x^3-2x^2  in math
    return 4*x**3-2*x**2


# ## derivative using the `diff` function

# In[7]:


x=linspace(-2,2,100)
y=f(x)
plot(x,y)


# In[8]:


x


# In[9]:


y


# In[16]:


dx=x[2]-x[1]
dfdx=diff(y)/dx
xf=x[:-1]
plot(xf,dfdx)
slope_expected=12*xf**2-4*xf
plot(xf,slope_expected,'r--')


# ## integrate with `scipy.integrate`

# In[18]:


import scipy.integrate


# In[23]:


y_int=scipy.integrate.cumulative_trapezoid(y,x)
plot(x[:-1],y_int)
area_expected=x**4-2*x**3/3
plot(x,area_expected,'r--')  # off by a constant

y_int=y_int-y_int[0]+area_expected[0]
plot(x[:-1],y_int,'c:')


# ## zeros with fancy indexing

# In[35]:


xf[:-1][sign(dfdx[:-1])!=sign(dfdx[1:])]


# In[ ]:





# In[ ]:




