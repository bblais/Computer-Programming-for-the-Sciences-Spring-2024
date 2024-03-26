#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# ![Screenshot 2024-03-21 at 12.21.30.png](attachment:d11bd26e-2d9c-42ea-815a-f8f25ef1357e.png)
# - Data: UUUDUDUUUUUD (3D, 9U in 12 flips)

# ## Models:
# 
# $\theta$ = probability of heads
# 
# 1. $H_5$ : $\theta=50\%$
# 1. $H_3$ : $\theta=30\%$
# 1. $H_7$ : $\theta=70\%$

# In[ ]:


P_data_H3 = 0.7**9 * 0.3**3
P_data_H5 = 0.5**9 * 0.5**3
P_data_H7 = 0.3**9 * 0.7**3

P_H3=1/3
P_H5=1/3
P_H7=1/3

P_data = P_data_H3 * P_H3 + P_data_H5 * P_H5 + P_data_H7 * P_H7

P_H3_given_data = P_data_H3 * P_H3 / P_data
P_H5_given_data = P_data_H5 * P_H5 / P_data
P_H7_given_data = P_data_H7 * P_H7 / P_data

print(P_H3_given_data, P_H5_given_data, P_H7_given_data)


# In[ ]:


h=3
N=12

θ=array([0.3, 0.5, 0.7])
prior=array([1/3, 1/3, 1/3])
likelihood=θ**h*(1-θ)**(N-h)
print(prior)
print(likelihood)

total=sum(prior*likelihood)
print(total)

posterior=prior*likelihood/total
print(posterior)


# In[ ]:


plot(θ, posterior,'-o')


# In[ ]:


h=3
N=12

θ=linspace(0,1,11)

θ


# In[ ]:


number_of_models=len(θ)
prior=ones(number_of_models)/number_of_models
prior


# In[ ]:


likelihood=θ**h*(1-θ)**(N-h)
print(prior)
print(likelihood)

total=sum(prior*likelihood)
print(total)

posterior=prior*likelihood/total
print(posterior)


# In[ ]:


plot(θ, posterior,'-o')
xlabel('θ')
ylabel('p(θ|data)')


# In[ ]:


h=3
N=12

θ=linspace(0,1,1000)
number_of_models=len(θ)
prior=ones(number_of_models)/number_of_models

likelihood=θ**h*(1-θ)**(N-h)

total=sum(prior*likelihood)

posterior=prior*likelihood/total

plot(θ, posterior,'-')
xlabel('θ')
ylabel('p(θ|data)')


# In[ ]:




