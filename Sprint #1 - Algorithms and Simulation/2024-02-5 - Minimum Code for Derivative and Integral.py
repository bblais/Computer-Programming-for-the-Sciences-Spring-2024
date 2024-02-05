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


# In[9]:


x_start=-2
x_end=2
dx=0.01


# ## derivative

# In[10]:


x=x_start
S=Storage()
while x<=x_end:

    # calculate the slope at that value (rise/run) = (f(x+dx)-f(x))/dx
    # add the calculated values to the Storage
    #step the x value by small step called dx

    slope=(f(x+dx)-f(x))/dx

    S+=x,slope
    
    x=x+dx

    
x,slope=S.arrays()


# In[11]:


plot(x,slope)
slope_expected=12*x**2-4*x
plot(x,slope_expected,'r--')


# ## integral

# In[12]:


x=x_start
S=Storage()
area=0
while x<=x_end:

    # calculate the area at that value
    # add the calculated values to the Storage
    #step the x value by small step called dx

    slope=(f(x+dx)-f(x))/dx
    area_rectangle=f(x)*dx
    area_triangle=1/2*dx*(f(x+dx)-f(x))
    area=area+area_rectangle+area_triangle
    
    S+=x,slope,area
    
    x=x+dx

    
x,slope,area=S.arrays()


# In[13]:


plot(x,area)

area_expected=x**4-2*x**3/3-(x_start**4-2*x_start**3/3)
plot(x,area_expected,'r--')


# In[ ]:




