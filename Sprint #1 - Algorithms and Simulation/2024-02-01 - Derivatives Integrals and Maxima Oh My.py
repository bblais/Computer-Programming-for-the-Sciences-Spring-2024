#!/usr/bin/env python
# coding: utf-8

# ## Outline for taking a derivative numerically
# 
# 
# 1. define a function (def statement)
# 2. specify start value for x and an end value for x
# 3. start a Storage for calculated values
# 4. set x value to the start value
# 5. calculate the slope at that value (rise/run) = (f(x+dx)-f(x))/dx
# 6. add the calculated values to the Storage
# 7. step the x value by small step called dx
# 8. repeat until x value is after the end value
# 9. at the end, plot the Stored values

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[2]:


def f(x):
    # f(x)=4x^3-2x^2  in math
    return 4*x**3-2*x**2


# In[10]:


x_start=-2
x_end=2
dx=0.1


# ## plot the function 

# In[12]:


x=linspace(x_start,x_end,500)
y=f(x)
plot(x,y)
ylim([-1,1])


# In[15]:


x=x_start
print(x)
S=Storage()
while x<=x_end:

    # calculate the slope at that value (rise/run) = (f(x+dx)-f(x))/dx
    # add the calculated values to the Storage
    #step the x value by small step called dx

    slope=(f(x+dx)-f(x))/dx

    S+=x,slope
    
    x=x+dx

    
x,slope=S.arrays()
x


# In[16]:


slope


# In[18]:


plot(x,slope)

slope_expected=12*x**2-4*x
plot(x,slope_expected,'r--')


# redo with smaller step size dx

# In[19]:


x_start=-2
x_end=2
dx=0.01

x=x_start
print(x)
S=Storage()
while x<=x_end:

    # calculate the slope at that value (rise/run) = (f(x+dx)-f(x))/dx
    # add the calculated values to the Storage
    #step the x value by small step called dx

    slope=(f(x+dx)-f(x))/dx

    S+=x,slope
    
    x=x+dx

    
x,slope=S.arrays()

plot(x,slope)

slope_expected=12*x**2-4*x
plot(x,slope_expected,'r--')


# In[21]:


x_start=-2
x_end=2
dx=0.01

x=x_start
S=Storage()
while x<=x_end:

    # calculate the area at that value
    # add the calculated values to the Storage
    #step the x value by small step called dx

    slope=(f(x+dx)-f(x))/dx
    area_rectangle=f(x)*dx
    area_triangle=1/2*dx*(f(x+dx)-f(x))
    area=area_rectangle+area_triangle
    
    S+=x,slope,area
    
    x=x+dx

    
x,slope,area=S.arrays()


# derivative is fine

# In[22]:


plot(x,slope)

slope_expected=12*x**2-4*x
plot(x,slope_expected,'r--')


# integral is way wrong

# In[23]:


plot(x,area)

area_expected=x**4-2*x**3/3
plot(x,area_expected,'r--')


# fixing the integral

# In[24]:


x_start=-2
x_end=2
dx=0.01

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


# off by a constant

# In[25]:


plot(x,area)

area_expected=x**4-2*x**3/3
plot(x,area_expected,'r--')


# yay!

# In[26]:


plot(x,area)

area_expected=x**4-2*x**3/3-(x_start**4-2*x_start**3/3)
plot(x,area_expected,'r--')


# In[ ]:




