#!/usr/bin/env python
# coding: utf-8

# ## Simulation
# 
# 1. set the parameters (e.g. a=0.0083)
# 2. set the initial value for variables (e.g. p=7e9)
# 3. set the simulation parameters (e.g. dt=0.1)
# 4. set t=0
# 5. loop
#    1. apply model equations  (e.g. dp/dt=a*p  -->  dp=a*p*dt)
#    2. update the variables and time (e.g. p=p+dp;  t=t+dt)

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
# make the plots appear in the notebook
from pylab import *  # be lazy about importing all the math and plotting functions
from sci378 import *  # be lazy about all the functions for the class


# ## Set the parameters

# In[15]:


a=0.0083


# ## Set the initial variables

# In[16]:


p=7e9


# ## Set the simulation parameters

# In[17]:


dt=0.1


# ## Set initial time

# In[18]:


t=0


# In[19]:


S=Storage()  # set up a storage to keep track of the calculations

S+=t,p  #  add the starting values to the storage
while t<10:

    # apply the model equations
    dp=a*p   # small change in p

    # update the variables and time
    p=p+dp
    t=t+dt

    S+=t,p  #  add the updated values to the storage

t,p=S.arrays()  # get the stored values as arrays so we can plot, etc...


# In[20]:


figure(figsize=(6,3))
plot(t,p);


# In[10]:





# In[23]:


a=0.0083
p=7e9
t=0
dt=0.1

S=Storage()  # set up a storage to keep track of the calculations

S+=t,p  #  add the starting values to the storage
while t<10:

    # apply the model equations
    dp=a*p   # small change in p

    # update the variables and time
    p=p+dp
    t=t+dt

    S+=t,p  #  add the updated values to the storage

t,p=S.arrays()  # get the stored values as arrays so we can plot, etc...


# In[24]:


plot(t,p)


# ## throwing a ball in the air

# In[29]:


# parameters
g=10

# initial variables
v=5
y=1.5

# time
t=0
dt=0.01


S=Storage()  # set up a storage to keep track of the calculations

S+=t,y,v  #  add the starting values to the storage
while t<2:

    # apply the model equations -- one for each variable
    dy=v*dt    #  dy/dt=v
    dv=-g*dt   #  dv/dt=-g

    # update the variables and time
    y=y+dy
    v=v+dv
    t=t+dt

    S+=t,y,v  #  add the updated values to the storage

t,y,v=S.arrays()  # get the stored values as arrays so we can plot, etc...


# In[30]:


figure(figsize=(6,3))
plot(t,y);
xlabel('time')
ylabel('height')


# In[31]:


figure(figsize=(6,3))
plot(t,v);
xlabel('time')
ylabel('speed')


# In[ ]:




