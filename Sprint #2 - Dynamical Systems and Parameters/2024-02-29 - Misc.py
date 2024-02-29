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


# ## Harmonic Oscillator
# 
# When comparing data to the harmonic oscillator, best to always compare to the $x$ variable.  Sometimes the data starts low and goes high.  Sometimes it starts high and goes low.  
# 
# - Set $x0$ to the mean value of the data
# - adjust $k$ for the number of bumps per time period (higher $k$ = more bumps). 
# - Adjust the initial conditions to deal with the high to low or low to high start.  

# In[37]:


t_data=linspace(0,10,100)
y_data=10*sin(3*t_data)+20
plot(t_data,y_data,'-o')


# In[44]:


sim=Simulation()
sim.add("x'=v",initial_value=20,plot=True)
sim.add("v'=-k*(x-x0)",initial_value=20)
sim.params(k=9,x0=20)
sim.add_data(t=t_data,x=y_data,plot=True)
sim.run(10)


# In[34]:


t_data=linspace(0,10,100)
y_data=10*cos(3*t_data)+20
plot(t_data,y_data,'-o')


# In[45]:


sim=Simulation()
sim.add("x'=v",initial_value=29,plot=True)
sim.add("v'=-k*(x-x0)",initial_value=0)
sim.params(k=9,x0=20)
sim.add_data(t=t_data,x=y_data,plot=True)
sim.run(10)


# In[ ]:




