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

# In[27]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[28]:


import pylab
pylab.__file__


# In[29]:


import sci378


# In[30]:


sci378.__file__


# In[31]:


def f(x):
    # f(x)=4x^3-2x^2  in math
    return 4*x**3-2*x**2


# In[32]:


def f(x):
    return sin(x)


# In[33]:


x_start=-2
x_end=4
dx=0.1


# ## plot the function 

# In[34]:


x=linspace(x_start,x_end,5)  # linspace spits out list of values.  the number of values is the last one (5 in this case)
x


# In[35]:


y=f(x)
y


# In[36]:


x=linspace(x_start,x_end,500)
y=f(x)
plot(x,y,'-')
#ylim([-1,1])


# In[37]:


x=x_start
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


# In[38]:


slope


# In[39]:


plot(x,slope)

slope_expected=12*x**2-4*x
slope_expected=cos(x)
plot(x,slope_expected,'r--')


# redo with smaller step size dx

# In[8]:


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


# In[9]:


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

# In[10]:


plot(x,slope)

slope_expected=12*x**2-4*x
plot(x,slope_expected,'r--')


# integral is way wrong

# In[11]:


plot(x,area)

area_expected=x**4-2*x**3/3
plot(x,area_expected,'r--')


# fixing the integral

# In[12]:


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

# In[13]:


plot(x,area)

area_expected=x**4-2*x**3/3
plot(x,area_expected,'r--')


# yay!

# In[14]:


plot(x,area)

area_expected=x**4-2*x**3/3-(x_start**4-2*x_start**3/3)
plot(x,area_expected,'r--')


# In[ ]:





# ## Maxima and Minima

# In[15]:


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
    previous_slope=(f(x)-f(x-dx))/dx

    if sign(slope)!=sign(previous_slope):  # when it changes sign it's a zero
        S+=x,f(x)
    
    x=x+dx

    
min_x,min_y=S.arrays()

# plot the function
x=linspace(x_start,x_end,500)
y=f(x)
plot(x,y)

plot(min_x,min_y,'ro')
ylim([-1,1])


# In[ ]:




