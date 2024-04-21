#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *
from lmfit import *


# ## Peak Fitting

# In[ ]:


data=pd.read_csv('data/peaks/sample0.csv')
data


# In[ ]:


t=array(data['t'])
y=array(data['y'])
plot(t,y,'o')


# In[ ]:


model=models.GaussianModel()
model.param_names


# In[ ]:


results=model.fit(y,x=t,
                 amplitude=1e7,
                 center=1,
                 sigma=0.1)
results


# In[ ]:


xx=linspace(0,2,1000)
yy=results.eval(x=xx)
plot(t,y,'o')
plot(xx,yy,'-')
xlim([.9,1.3])


# In[ ]:


def fit_peak(filename):
    data=pd.read_csv(filename)
    t=array(data['t'])
    y=array(data['y'])
    
    model=models.GaussianModel()
    params=model.make_params()
    
    
    
    
    params['amplitude']=Parameter("amplitude",
                                 min=0,
                                 value=max(y))
    
    results=model.fit(y,params,x=t,center=1,sigma=1)

    return t,y,results

def fit_peak_take2(filename):
    data=pd.read_csv(filename)
    t=array(data['t'])
    y=array(data['y'])
    
    model=models.GaussianModel() + models.LinearModel()
    params=model.make_params()
    
    
    params['amplitude']=Parameter("amplitude",
                                 min=0,
                                 value=max(y))

    params['offset']=Parameter("offset",
                                 value=(y[-1]+y[0])/2)
    params['slope']=Parameter("slope",
                                 value=(y[-1]-y[0])/(t[-1]-t[0]))
    
    
    results=model.fit(y,params,x=t,center=1,sigma=1)

    return t,y,results



# In[ ]:


t,y,results=fit_peak('data/peaks/sample0.csv')
xx=linspace(0,2,1000)
yy=results.eval(x=xx)
plot(t,y,'o')
plot(xx,yy,'-')
xlim([.9,1.3])


# In[ ]:


t,y,results=fit_peak('data/peaks/sample90.csv')
xx=linspace(0,2,1000)
yy=results.eval(x=xx)
plot(t,y,'o')
plot(xx,yy,'-')
xlim([.9,1.3])


# In[ ]:


t,y,results=fit_peak_take2('data/peaks/sample90.csv')
xx=linspace(0,2,1000)
yy=results.eval(x=xx)
plot(t,y,'o')
plot(xx,yy,'-')
xlim([.9,1.3])


# In[ ]:


from glob import glob


# In[ ]:


filenames=glob('data/peaks/sample*.csv')
len(filenames)


# In[ ]:


filenames[:5]


# In[ ]:


filenames[6]


# In[ ]:


count=1
for name in filenames[:12]:
    subplot(3,4,count)
    t,y,results=fit_peak_take2(name)
    xx=linspace(0,2,1000)
    yy=results.eval(x=xx)
    plot(t,y,'o')
    plot(xx,yy,'-')
    xlim([.9,1.3])
    
    count=count+1


# In[ ]:


t,y,results=fit_peak_take2('data/peaks/sample372.csv')
xx=linspace(0,2,1000)
yy=results.eval(x=xx)
plot(t,y,'o')
plot(xx,yy,'-')
#xlim([.9,1.3])


# In[ ]:


filenames[8]


# ## Logistic Function
# 
# $$
# f(x)=\frac{a}{1+\exp(-c(x-d))}+b
# $$
# 

# In[ ]:


data=pd.read_csv('data/logistic_sample_data/logistic_sample_data_0.csv')
data.head()


# In[ ]:


data=pd.read_csv('data/logistic_sample_data/logistic_sample_data_3.csv')


# In[ ]:


t=array(data['t'])
y=array(data['y'])
plot(t,y,'o')


# In[ ]:


def f(x,a=1,b=1,c=1,d=1):
    return a/(1+exp(-c*(x-d)))+b


# In[ ]:


xx=linspace(0,50,1000)
yy=f(xx,a=300,b=1,c=1,d=5)

plot(t,y,'o')
plot(xx,yy,'-')


# In[ ]:


model=Model(f)
params=model.make_params()
params['a']=Parameter("a",min=0,max=1000,value=200)
params['b']=Parameter("b",min=0,max=1000,value=10)
params['c']=Parameter("c",min=0,max=5,value=1)
params['d']=Parameter("d",min=-1000,max=1000,value=1)
results=model.fit(y,params,x=t)
results


# In[ ]:


plot(t,y,'o')

tt=linspace(0,50,300)
yy=results.eval(x=tt)
plot(tt,yy,'-')


# In[ ]:


def fit_logistic(filename,display=False):
    data=pd.read_csv(filename)
    t=data['t']
    y=data['y']
    model=Model(f)   # from lmfit
    params=model.make_params()
    params['a']=Parameter("a",min=0,max=1000,value=max(y))
    params['b']=Parameter("b",min=0,max=1000,value=1)
    params['c']=Parameter("c",min=0,max=5,value=1)
    params['d']=Parameter("d",min=-1000,max=1000,value=1)

    result = model.fit(y, params, x=t)
    
    
    if display:
        plot(t,y,'o')
        tt=linspace(0,50,300)
        yy=result.eval(x=tt)
        plot(tt,yy,'-')     
        
    return result


# In[ ]:


fit_logistic('data/logistic_sample_data/logistic_sample_data_3.csv',display=True)


# In[ ]:


filenames=glob('data/logistic_sample_data/log*.csv')
count=1
for name in filenames[:12]:
    subplot(3,4,count)
    fit_logistic(name,True)
    count=count+1


# ## World Population

# In[ ]:


data=pd.read_excel('data/Appendix_ World Population Estimate Sets.xlsx',skiprows=2)
data.head()


# In[ ]:


t=data['Time']
y=data['population']
plot(t,y,'o')


# In[ ]:


t=(data['Time'].dropna()-(-10000))/1000
y=data['population'].dropna()

plot(t,y,'o')

y=array(y[t>11])
t=array(t[t>11])
t=t-min(t)
plot(t,y,'o')


# In[ ]:


plot(t,y,'o')


# $$
# N=N_1 \left(\frac{t_o-t_1}{t_0-t}  \right)^k
# $$

# In[ ]:


def N(x,k,to,N1,t1):
    return N1*((to-t1)/(to-x))**k


# In[ ]:


model=Model(N)
params=model.make_params()
params


# In[ ]:


params['to']=Parameter("to",min=max(t)+1e-4,max=1000,value=max(t)+50)
params['k']=Parameter("k",min=0,max=20,value=.1)
params['N1']=Parameter("N1",value=y[0],vary=False)
params['t1']=Parameter("t1",value=t[0],vary=False)
params


# In[ ]:


result = model.fit(y, params, x=t)
result


# In[ ]:


plot(t,y,'o')
tt=linspace(0,0.91,300)
yy=result.eval(x=tt)
plot(tt,yy,'-')  


# In[ ]:





# In[ ]:




