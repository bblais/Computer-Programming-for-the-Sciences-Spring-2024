#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# ## Load all the data

# Somehow Excel can't handle 19000 columns.  😀

# ![image.png](attachment:91d2d916-b980-428d-963a-6bbe8e8ec26b.png)

# In[ ]:


data=pd.read_csv('data/crichton/time series data pandas.csv.zip')
data.head()


# In[ ]:


station_data=pd.read_excel('data/crichton/station_info.xlsx')
station_data


# ## Searching for names

# In[ ]:


station_data[station_data['Station'].str.contains('KOLN')]


# ## Plot one of the columns

# In[ ]:


t,y=data['time'],data['KOLN_BONN']
plot(t,y,'-o')


# ## Copying from the fitting functions notebook

# In[ ]:


def get_temperature_time_slope(station_name,plotit=False):
    from lmfit.models import LinearModel
    
    t,y=data['time'],data[station_name]

    t=t.values[y<500]  # just in case there are weird 999 numbers
    y=y.values[y<500]    
    
    if plotit:
        plot(t,y,'-o')
        
    mymodel=LinearModel()
    result=mymodel.fit(y,x=t)  
    
    if plotit:
        tt=linspace(min(t),max(t),100)
        yy=result.eval(x=tt)
        plot(tt,yy,'r-')


        text(min(t)+5,max(y)-.1,
             f"$y={result.params['slope'].value:.4f}x+{result.params['intercept'].value:.4f}$")    
    
        title(station_name)
    return result.best_values['slope']


# In[ ]:


get_temperature_time_slope('KOLN_BONN')


# In[ ]:


get_temperature_time_slope('KOLN_BONN',plotit=True)


# # Solving the Crichton Problem
# 
# - Crichton's claim:
#     - CO$_2$ does not drive temperature -- it's urban development
#     - urban temperatures have increased over time, but the nearby rural (i.e. undeveloped) areas have not
#     
# - This means that the slope of urban areas should be positive and close rural areas should be near zero or negative
# 
# 
# ### Outline
# 
# - Go through all of the stations with BI>10 (urban)
#     - for each urban station, find the nearest rural save the pair of (urban slope, rural slope).  We'll call U the urban slope and R the rural slope.
# - make a plot of rural slopes vs urban slopes
# - Crichton's claim then implies a certain structure of the plot of all these points
#     - global warming would have U>0 and R>0, so dots in the upper right
#     - Crichton claims that U>0 and R<0, so dots in the lower right
#     - global cooling would have U<0 and R<0, so dots in the lower left
#     - there's a weird corner with U<0 and R>0 -- urban cooling rural warming where there shouldn't be any points

# The only thing missing is some way to find the neasest rural, once we have a station.  
# 
# - The station data has latitude and longitude.  
# - the station data has a brightness index, BI>10 for urban

# In[ ]:


station_data['urban']=station_data['Brightness']>10


# In[ ]:


station_data


# In[ ]:


def closest_rural(name):
    
    # get the location of the named urban site
    latitude_site=float(station_data[station_data['Station']==name]['Latitude'].iloc[0])
    longitude_site=float(station_data[station_data['Station']==name]['Longitude'].iloc[0])

    # calculate the distance away for all stations...
    station_data['dsquared']=(station_data['Latitude']-latitude_site)**2+(station_data['Longitude']-longitude_site)**2    
    # sort by that distance
    sorted_station_data=station_data.sort_values('dsquared')
    
    # find the closest rural station
    rural_site=sorted_station_data.query('urban==False').iloc[0]
    
    return rural_site['Station']


# In[ ]:


closest_rural('KOLN_BONN')


# ## Now go through the outline

# - For each urban station, find the nearest rural save the pair of (urban slope, rural slope).  We'll call U the urban slope and R the rural slope.

# Since this may take a while, use the (weirdly named) tqdm library to show progress.

# In[ ]:


from tqdm import tqdm


# In[ ]:


names=list(station_data.query('urban==True')['Station'])
print("Number of urban sites:",len(names))


# In[ ]:


U=[]
R=[]
for name in tqdm(names):
    U.append(get_temperature_time_slope(name,plotit=False))
    rural_name=closest_rural(name)
    R.append(get_temperature_time_slope(rural_name,plotit=False))


# In[ ]:


plot(U,R,'o',alpha=.1)
axis('equal')


# ## Questions to explore
# 
# - How do the means of the slopes differ between urban and rural?
# - How do the standard deviations of the slopes differ between urban and rural?
# - What does this mean?
# - Is there any evidence of upward curvature in the temperature-time curves for urban sites?  (i.e. fit to a quadratic, and look for values of "a" greater than zero)
# - What about for rural sites?

# In[ ]:




