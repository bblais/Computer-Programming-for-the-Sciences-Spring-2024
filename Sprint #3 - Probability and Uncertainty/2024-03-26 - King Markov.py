#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# https://www.youtube.com/watch?v=Qqz5AJjyugM&t=363s
# 
# 
# ![Screenshot 2024-03-24 at 08.34.07.png](attachment:49fcd7bc-74ce-4c8f-a6c4-a53ea07a61c0.png)
# 
# 

# In[ ]:


N=10
population=arange(1,N+1)*10
population


# In[ ]:


location=0
N_steps=10000

S=Storage()



for i in range(N_steps):
    S+=location,
    flip=rand()>0.5  # choose left or right
    if flip:
        proposal=location+1
    else:
        proposal=location-1
    proposal=proposal%N  # wrap around
    
    
    proposal_pop=population[proposal]
    current_pop=population[location]

    if N_steps<20:
        print(i,location,proposal,proposal_pop,current_pop)
        
    r=rand()
    if r<(proposal_pop/current_pop):
        location=proposal
        if N_steps<20:
            print(r,"accepted")
    else:
        if N_steps<20:
            print(r,"rejected")


y=S.arrays()
#print(y)
hist(y,bins=arange(-.5,N+.5),width=0.5);


# In[ ]:


plot(y)


# In[ ]:


x=linspace(-5,5,N)
population=np.round(exp(-x**2/2/2)*1000)  # make up a more interesting population distribution
population


# In[ ]:


plot(population,'-o')


# In[ ]:


location=0


S=Storage()



for i in range(10000):
    S+=location,
    flip=rand()>0.5
    if flip:
        proposal=location+1
    else:
        proposal=location-1
    proposal=proposal%N  # wrap around
    proposal_pop=population[proposal]
    current_pop=population[location]

    #print(i,location,proposal,proposal_pop,current_pop)
    r=rand()
    if r<(proposal_pop/current_pop):
        location=proposal
        #print(r,"accepted")
    else:
        pass
        #print(r,"rejected")


y=S.arrays()
#print(y)
hist(y,bins=arange(-.5,N+.5),width=0.5);


# In[ ]:


plot(y,'k-')


# In[ ]:




