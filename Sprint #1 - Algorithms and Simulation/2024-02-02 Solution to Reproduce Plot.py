#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# ![pone.0174411.g005.png](attachment:d56d454f-3685-477c-bcc4-13361d4fc530.png)

# In[2]:


data=pd.read_csv('data/greenyellowarrow.csv')
data


# In[3]:


x=data['green x']
y=data['green y']

plot(x,y,'g^',markersize=10,label='Evergreen')

text(x[0]+.04,y[0],'ZS')
text(x[1]+.01,y[1],'KC')
text(x[2]+.04,y[2]-.05,'HB')


x=data['yellow x']
y=data['yellow y']

plot(x,y,'yv',label='Deciduous')

axis('equal')
axis('square')
xlim([-1,1])
ylim([-1,1])
grid(False)

plot([-1,1],[0,0],'k--')
plot([0,0],[-1,1],'k--')

xa=data['arrow x']
ya=data['arrow y']

for x,y in zip(xa,ya):
    plot([0,x],[0,y],'r.-')


xlabel('Axis 1 (75.1%)')
ylabel('Axis 2 (13.7%)')
legend()


# In[ ]:




