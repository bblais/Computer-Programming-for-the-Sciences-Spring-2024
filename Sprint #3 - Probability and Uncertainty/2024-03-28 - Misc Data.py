#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
chronic_kidney_disease = fetch_ucirepo(id=336) 
  
# data (as pandas dataframes) 
X = chronic_kidney_disease.data.features 
y = chronic_kidney_disease.data.targets 
  


# In[ ]:


from numpy import array


# In[ ]:


y


# In[ ]:


X.columns


# In[ ]:


array(X[y['class'] == 'ckd']['sod'].dropna())


# In[ ]:


array(X[y['class'] == 'notckd']['sod'].dropna())


# In[ ]:




