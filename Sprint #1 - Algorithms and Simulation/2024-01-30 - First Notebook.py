#!/usr/bin/env python
# coding: utf-8

# # Header
# 
# ## Subheading
# 
# some text.
# 
# ### sub sub heading
# 
# ## another subheading
# 
# I can do **bold** and *italic*.  Even equations (use LaTeX format):
# 
# $$
# E=mc^2 \times \sqrt{\frac{1}{1-v^2/c^2}}
# $$
# 

# In[1]:


a=5


# In[2]:


a


# In[3]:


b=10
a+b


# In[4]:


a*b


# Exponents use ** not ^

# In[5]:


3**4


# In[6]:


3^4  # gives a weird answer and is not an exponent


# In[7]:


a


# In[8]:


a=a+1


# In[9]:


a


# In[11]:


bob=56
sally=103
bob*sally


# In[13]:


print("here")
for i in range(10):
    print(i)
    print("hello")

    print("another")

print("there")


# In[14]:


print("here")
for bob in range(10):
    print(bob,"hello")

print("there")


# In[16]:


S=0
for value in range(10):
    print("before",S)
    S=S+value
    print("after",S)

print(S)


# In[18]:


S=0
for value in range(10):
    S=S+value

print(S)


# In[17]:


0+1+2+3+4+5+6+7+8+9


# ### Wrong way #1

# In[19]:


N=15

# rest of this I want at the end to print out the factorial of N

total=0
for value in range(N):
    total=total*value

print(total) 


# the range(N) goes from 0 to N-1

# ### Wrong way #2 

# In[20]:


N=15

# rest of this I want at the end to print out the factorial of N

total=0
for value in range(1,N+1):
    print(value)
    total=total*value

print(total) 


# In[21]:


N=15

# rest of this I want at the end to print out the factorial of N

total=0
for value in range(N):
    print(value)
    total=total*(value+1)

print(total) 


# ### hopefully correct

# In[23]:


N=15

# rest of this I want at the end to print out the factorial of N

total=1
for value in range(N):
    total=total*(value+1)

print(total) 


# In[24]:


def factorial(N):
    total=1
    for value in range(N):
        total=total*(value+1)

    return total


# In[25]:


a=factorial(5)


# In[26]:


print(a)


# Our friend Pythagoras:
# 
# $$
# a^2 + b^2 = c^2
# $$
# 
# which means
# 
# $$
# c=\sqrt{a^2 + b^2}
# $$

# In[27]:


a=5
b=8
c=sqrt(a**2+b**2)


# In[28]:


from numpy import sqrt


# In[29]:


a=5
b=8
c=sqrt(a**2+b**2)


# In[30]:


print(c)


# In[ ]:




