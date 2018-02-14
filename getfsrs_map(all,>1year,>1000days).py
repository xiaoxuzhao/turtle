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
a=fig.add_subplot(1,3,1)
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
a.set_title('All sites with raw data',fontsize=10)
my_map.drawparallels(np.arange(40,80,3),labels=[1,0,0,0])
my_map.drawmeridians(np.arange(-180,180,3),labels=[1,1,0,1])
a=fig.add_subplot(1,3,2)
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
a.set_title('Longterm sites (>1 year)',fontsize=10)
my_map.drawparallels(np.arange(40,80,3),labels=[0,0,0,1])
my_map.drawmeridians(np.arange(-180,180,3),labels=[1,1,0,1])
a=fig.add_subplot(1,3,3)
Lat=[43.470399999999998, 43.556800000000003,
     43.691699999999997, 43.647500000000001, 
     43.466200000000001, 43.8782, 43.421999999999997, 
     43.479700000000001, 43.773299999999999, 43.686199999999999]
Lon=[-65.762299999999996, -65.920000000000002,
     -65.209699999999998, -65.913700000000006, 
     -65.674999999999997, -64.766300000000001, 
     -65.711699999999993, -65.445999999999998,
     -66.228300000000004, -65.861000000000004]
my_map = Basemap(projection='lcc', lat_0 = 45, lon_0 = -63,
    resolution = 'h', area_thresh = 0.3,
    llcrnrlon=-68, llcrnrlat=42.0,
    urcrnrlon=-59, urcrnrlat=48) 
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'coral')
my_map.drawmapboundary()
x,y=my_map(Lon,Lat)
my_map.plot(x, y, 'bo', markersize=4)
a.set_title('Longterm sites (>1000 days)',fontsize=10)
my_map.drawparallels(np.arange(40,80,3),labels=[0,0,0,1])
my_map.drawmeridians(np.arange(-180,180,3),labels=[1,1,0,1])
plt.savefig('compare_getfsrs_map',dpi=200) 
plt.show()

