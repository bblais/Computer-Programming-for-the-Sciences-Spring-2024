#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *
from sci378.stats import *


# In[ ]:


data=pd.read_csv('data/dog_mass.csv')
t_data=data['days'].values[:10]  # just the start
y_data=data['mass'].values[:10]
data


# In[ ]:




