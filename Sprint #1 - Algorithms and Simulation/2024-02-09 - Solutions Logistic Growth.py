#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# $$
# \frac{dx}{dt}=ax\left(1-\frac{x}{K}\right)
# $$
# 
# multiply both sides by $dt$:
# 
# $$
# dx=\left(ax\left(1-\frac{x}{K}\right)\right)\cdot dt
# $$

# ## set initial conditions for variables

# In[2]:


x=2
t=0
dt=0.01


# ## set values of parameters

# In[3]:


a=1
K=10


# ## loop the model equations
# 
# - calculate small changes in the variables
# - update variables

# In[4]:


S=Storage()

S+=t,x

while t<10:
    
    dx = (a*x*(1-x/K)) *dt  # small change in x
    
    x=x+dx # update the variables with small changes
    t=t+dt
    
    S+=t,x  # stores the calculated values for plotting

    
t,x=S.arrays()


# In[5]:


plot(t,x)


# ## Parameter exploration

# In[6]:


for a in [0.5,1,2]:

    x=2
    t=0
    dt=0.01

    #a=1  # this is set by the loop
    K=10

    S=Storage()

    S+=t,x

    while t<10:

        dx = (a*x*(1-x/K)) *dt  # small change in x

        x=x+dx # update the variables with small changes
        t=t+dt

        S+=t,x  # stores the calculated values for plotting


    t,x=S.arrays()

    plot(t,x,label=f'a={a}')
    
legend()


# In[7]:


for K in [1,10,20]:

    x=2
    t=0
    dt=0.01

    a=1  
    #K=10 # this is set by the loop

    S=Storage()

    S+=t,x

    while t<10:

        dx = (a*x*(1-x/K)) *dt  # small change in x

        x=x+dx # update the variables with small changes
        t=t+dt

        S+=t,x  # stores the calculated values for plotting


    t,x=S.arrays()

    plot(t,x,label=f'K={K}')
    
legend()


# In[8]:


figure(figsize=(20,20))
count=1
for K in [1,10,20]:
    for a in [0.5,1,2]:

        subplot(3,3,count)
        count+=1
        
        x=2
        t=0
        dt=0.01

        #a=1  
        #K=10 # this is set by the loop

        S=Storage()

        S+=t,x

        while t<10:

            dx = (a*x*(1-x/K)) *dt  # small change in x

            x=x+dx # update the variables with small changes
            t=t+dt

            S+=t,x  # stores the calculated values for plotting


        t,x=S.arrays()

        plot(t,x)
        title(f'a={a},K={K}')


# In[ ]:




