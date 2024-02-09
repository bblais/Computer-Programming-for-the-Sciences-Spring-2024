#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# ## Some Rules for good plots
# 
# 1. the fonts should be at least 20pt, but be proportional to the figure size and not look small
# 2. labels on axes and title
# 3. proper use of serif vs sans-serif fonts
# 4. use of markers in the plot for data (as opposed to models, theory, or equations)
# 5. lines in addition to markers for time-series, or where it is clear
# 6. axes make sense and don’t distort the data
# 7. legends/text should not waste real-estate
# 8. high content/ink ratio
# 9. titles and axis labels should have units
# 10. titles and axis labels should not be redundant
# 11. colors should be reasonable — 
#     1. models/trendlines should match the data
#     2. distinct colors for distinct quantities
#     3. comparable colors for comparable quantities

# In[2]:


data=pd.read_excel('data/alces.xlsx')


# In[3]:


data.head()


# In[4]:


x=array(data['year'])
y=array(data['individuals'])
plot(x,y,'-o')
xlabel('Year')
ylabel('Number of Alces alces moose')


# In[ ]:





# In[ ]:




