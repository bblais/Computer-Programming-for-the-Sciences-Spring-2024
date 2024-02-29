#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from pyndamics3 import Simulation
import pandas as pd


# In[4]:


ls data


# In[12]:


data=pd.read_csv("data/vostok.icecore.co2.txt",skiprows=20,sep="\t",header=None)
data.columns=["depth","ice age","gas age","co2"]
data


# In[17]:


t_data=data["gas age"][:10]
y_data=data["co2"][:10]
plot(t_data,y_data,'-o')
xlabel("time (ka)")
ylabel("co2 concentration (ppm)")
grid()


# In[19]:


t_data=t_data-t_data[0]  # one way to set the data to start at zero

# or alternatively
t_data=t_data-t_data.min()  # one way to set the data to start at zero

# you don't need both

plot(t_data,y_data,'-o')
xlabel("time (ka)")
ylabel("co2 concentration (ppm)")
grid()


# In[ ]:




