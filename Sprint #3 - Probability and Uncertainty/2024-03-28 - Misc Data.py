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


for key in [ 'sod', 'pot', 'hemo', 'pcv', 'wbcc', 'rbcc']:
    xx=list(X[y['class'] == 'ckd'][key].dropna())    
    yy=list(X[y['class'] == 'notckd'][key].dropna())
    print(f"{key}_with_disease=",xx)
    print(f"{key}_without_disease=",yy)
    print()


# In[ ]:


S="""age,height
27,161.04932824512468
27,157.9426178709342
28,164.1788887695886
29,163.5444584776847
29,160.0677105870573
29,163.4570784506083
27,168.07863142839346
30,165.5842439573259
29,164.60559623405865
30,162.37256998934072
29,160.85236511580408
27,159.47788764805034
30,160.31123408359386
27,161.94652961732714
27,163.24033248763644
28,161.395775470153
29,162.663444246199
28,163.54501256491702
27,160.47064474126054
27,159.17020422001926
29,164.70719276324408
29,161.734440900764
28,159.57127502414204
29,162.96029708877256
28,158.41041088210005
"""


# In[ ]:


vals=[]
for line in S.strip().split("\n")[1:]:
    parts=line.split(",")
    vals.append(round(float(parts[-1]),2))
    
print(vals)


# In[ ]:


S="""
age,height
38,158.50520380138045
38,155.78634830073162
37,159.58138925854183
40,161.6786105351603
40,155.75106537745432
39,158.05978286474604
39,159.63631666952753
37,168.2565438032523
39,162.87113378047627
37,156.97645741414237
39,157.5994283721841
39,159.34514365989384
38,159.1108384263324
40,155.9876140009476
40,155.75821383963873
38,152.07879641137774
40,158.7674330206936
37,155.18652001285315
37,165.5937580438753
40,156.94580701925483
38,159.45637143478692
39,160.89030152727707
40,158.7787727086037
39,156.5902675783446
40,155.9838976379255
"""


# In[ ]:


vals=[]
for line in S.strip().split("\n")[1:]:
    parts=line.split(",")
    vals.append(round(float(parts[-1]),2))
    
print(vals)


# In[ ]:




