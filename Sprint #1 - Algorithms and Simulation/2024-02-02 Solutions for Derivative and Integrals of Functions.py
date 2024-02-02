#!/usr/bin/env python
# coding: utf-8

# - https://www.wolframalpha.com/input?i=sin%2820*x%29*exp%28-x%5E2%29%2B10*exp%28-x%5E2%29
# 
# ![image.png](attachment:830743bd-b150-4b92-ac17-140b12fdd0ca.png)
# 
# - https://www.wolframalpha.com/input?i=derivative+of+sin%2820*x%29*exp%28-x%5E2%29%2B10*exp%28-x%5E2%29
# 
# ![image.png](attachment:b64b41e0-1398-463b-b593-e56ba2cbaba4.png)
# 
# - https://www.wolframalpha.com/input?i=integral+of+sin%2820*x%29*exp%28-x%5E2%29%2B10*exp%28-x%5E2%29
# 
# ![image.png](attachment:3189f8d4-68f1-4c29-a019-dbc02ab707af.png)

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[2]:


def fun(x):
    return sin(20*x)*exp(-x**2)+10*exp(-x**2)


# In[3]:


x=linspace(-5,5,300)
y=fun(x)
plot(x,y)


# ## Derivative

# In[4]:


x_start=-5
x_end=5
step=0.01

S=Storage()

x=x_start
while x<=x_end:
    
    # print(x," ",end="")
    
    y_left=fun(x-step/2)
    y_right=fun(x+step/2)
    
    m=(y_right-y_left)/(step) # rise over run
    
    S+=x,m   # saving the result for later
    
    x=x+step
    
print("done.")

x,m=S.arrays()  # give me the saved results as two arrays


# In[5]:


def dfun_dx(x):
    return exp(-x**2) *(20*cos(20*x) - 2*x*(10 + sin(20*x)))


# In[6]:


plot(x,m,'b-')  # the numerical derivative

x_expected=linspace(-5,5,100)
y_expected=dfun_dx(x_expected)  # this is the expected from calculus

plot(x_expected,y_expected,'r--')


# ## Integral

# In[7]:


x_start=-5
x_end=5
step=0.01

S=Storage()

x=x_start
total_area=0
while x<=x_end:
        
    y_left=fun(x-step/2)
    y_right=fun(x+step/2)
    
    area_rect=y_right*step
    area_tri=(1/2)*step*(y_left-y_right)
    
    total_area=total_area+area_rect+area_tri
    
    
    S+=x,total_area   # saving the result for later
    
    x=x+step
    
print("done.")

x,total_area=S.arrays()  # give me the saved results as two arrays


# In[8]:


def int_fun(x):
    from scipy.special import erf
    return 5*sqrt(pi)*erf(x)  # - (sqrt(pi)*erfi(10 - sqrt(-1)*x))/(4*e**100) - (sqrt(pi)*erfi(10 + sqrt(-1)*x))/(4*e**100)


# In[9]:


plot(x,total_area,'b-')  # the numerical integral

x_expected=linspace(-5,5,100)
y_expected=int_fun(x_expected)-int_fun(x_start)

plot(x_expected,y_expected,'r--')


# ## Minimum and maximum

# do the derivative and select where it is zero (or crosses the x axis)

# In[10]:


def dfun_dx(x,step=0.01):
    y_left=fun(x-step/2)
    y_right=fun(x+step/2)
    

    m=(y_right-y_left)/(step) # rise over run
    
    return m


# In[11]:


dfun_dx(2)


# In[12]:


x_start=-5
x_end=5
step=0.01

S=Storage()

x=x_start
number_of_steps=0
while x<=x_end:
    
    # print(x," ",end="")
    
    y_left=dfun_dx(x-step/2)
    y_right=dfun_dx(x+step/2)
    
    if sign(y_left)!=sign(y_right):
        S+=x,y_left, y_right  # saving the result for later
    
    x=x+step
    number_of_steps=number_of_steps+1
    
print("done...",number_of_steps)

x,y_left, y_right=S.arrays()  # give me the saved results as two arrays

x,y_left, y_right


# In[13]:


# plot the function
xx=linspace(-5,5,300)
yy=fun(xx)
plot(xx,yy)

plot(x,fun(x),'ro')


# In[ ]:





# In[ ]:




