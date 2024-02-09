#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# $$
# d=\frac{v \cos \theta}{g}\left(v \sin \theta+\sqrt{v^2 \sin ^2 \theta+2 g y_0}\right)
# $$
# 
# $$
# d=\frac{v^2}{g} \sin 2 \theta
# $$

# In[2]:


def dfun_dx(x,step=0.01):
    y_left=fun(x-step/2)
    y_right=fun(x+step/2)
    

    m=(y_right-y_left)/(step) # rise over run
    
    return m


# In[3]:


def fun(θ):
    v=1
    g=10
    
    return v**2/g*sin(2*θ)


# In[4]:


def fun(θ):
    v=1
    g=10
    yo=3
    
    return v*cos(θ)/g*(v*sin(θ)+sqrt(v**2*sin(θ)**2+2*g*yo))


# In[5]:


θ=linspace(0,90,300)
d=fun(radians(θ))
plot(θ,d)


# In[6]:


x_start=0
x_end=90
step=0.01

S=Storage()

x=x_start
number_of_steps=0
while x<=x_end:
    
    # print(x," ",end="")
    
    y_left=dfun_dx(radians(x)-step/2)
    y_right=dfun_dx(radians(x)+step/2)
    
    if sign(y_left)!=sign(y_right):
        S+=x,y_left, y_right  # saving the result for later
    
    x=x+step
    number_of_steps=number_of_steps+1
    
print("done...",number_of_steps)

x,y_left, y_right=S.arrays()  # give me the saved results as two arrays

x,y_left, y_right


# ## Secant method
# 
# https://en.wikipedia.org/wiki/Secant_method
# 
# ![image.png](attachment:7a2dbe3f-d4ca-478d-bd14-f1ff70d754d9.png)

# In[7]:


x0=30
x1=60
tol=0.00001
number_of_steps=0

while abs(x1-x0)>tol:
    
    x2=x1-dfun_dx(radians(x1))*(x1-x0)/(dfun_dx(radians(x1))-dfun_dx(radians(x0)))
    
    x0=x1
    x1=x2

    number_of_steps+=1
    
print("done...",number_of_steps)
x1


# ## using scipy fmin on the original

# In[8]:


from scipy.optimize import fmin


# In[9]:


def fun(θ):
    v=1
    g=10
    yo=3
    
    return v*cos(θ)/g*(v*sin(θ)+sqrt(v**2*sin(θ)**2+2*g*yo))


# In[10]:


def negfun(θ):
    return -fun(θ)


# In[11]:


degrees(fmin(negfun,radians(45)))


# In[ ]:




