#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[2]:


a=linspace(-5,5,21)
a


# In[3]:


a=linspace(-5,5,27)
a


# In[4]:


a=linspace(-5,5,21)
2*a


# In[5]:


x=linspace(-5,5,21)
y=2*x-3
plot(x,y)

y=2*x**2-2*x+3
plot(x,y)


# In[6]:


x=linspace(-5,5,11)
y=2*x-3
plot(x,y,'-o')

y=2*x**2-2*x+3
plot(x,y,'-x')


# In[7]:


x=linspace(-5,5,21)
y=2*x-3
plot(x,y,label='Blue')

y=2*x**2-2*x+3
plot(x,y,label='Orange')

xlabel('Bacon')
ylabel('Eggs')
legend()


# In[8]:


import pandas as pd


# In[9]:


data=pd.read_excel('data/object1_data.xlsx')
data


# In[15]:


t_data=array(data['t'])
y_data=array(data['y'])
plot(t_data,y_data,'bo')

t=linspace(0,.6,100)
y=-.5*t**2-2*t+2
plot(t,y,'b-',label='$-.5t^2-2t+2$')

legend()


# In[ ]:




