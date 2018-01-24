# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:12:29 2018

@author: xiaoxu
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv
dfh=read_csv('fsrs_sites.csv')
dfh1=read_csv('getfsrs.csv')
fig = plt.figure()
a=fig.add_subplot(1,2,1)
my_map = Basemap(projection='lcc', lat_0 = 45, lon_0 = -63,
    resolution = 'h', area_thresh = 0.3,
    llcrnrlon=-68, llcrnrlat=42.0,
    urcrnrlon=-59, urcrnrlat=48) 
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'coral')
my_map.drawmapboundary() 
x,y=my_map(dfh1['Longitude'].values,dfh1['Latitude'].values)
my_map.plot(x, y, 'bo', markersize=4)
a.set_title('All sites with raw data',fontsize=15)
my_map.drawparallels(np.arange(40,80,3),labels=[1,0,0,0])
my_map.drawmeridians(np.arange(-180,180,3),labels=[1,1,0,1])
a=fig.add_subplot(1,2,2)
my_map = Basemap(projection='lcc', lat_0 = 45, lon_0 = -63,
    resolution = 'h', area_thresh = 0.3,
    llcrnrlon=-68, llcrnrlat=42.0,
    urcrnrlon=-59, urcrnrlat=48) 
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'coral')
my_map.drawmapboundary() 
x,y=my_map(dfh['Longitude'].values,dfh['Latitude'].values)
my_map.plot(x, y, 'bo', markersize=4)
a.set_title('Longterm sites (>1 year)',fontsize=15)
my_map.drawparallels(np.arange(40,80,3),labels=[0,0,0,1])
my_map.drawmeridians(np.arange(-180,180,3),labels=[1,1,0,1])
plt.savefig('compare_getfsrs_map',dpi=200) 
plt.show()
