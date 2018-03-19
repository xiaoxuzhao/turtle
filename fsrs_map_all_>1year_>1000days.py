# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:12:29 2018
@author: xiaoxu
map with different sites
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv
#####################
#HARDCODES
input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
save_dir='/home/zdong/xiaoxu/FSRS/figure/'
#####################
df_fsrs=read_csv(input_dir+'fsrs_sites(>1 km,year).csv')  #fsrs_sites(>1 km,year).py
df_getfsrs=read_csv(input_dir+'getfsrs.csv')          #fsrs_sites(>1 km,year).py
df_fsrs_1000=read_csv(input_dir+'fsrs_sites(>1000days).csv')   #fsrs_sites(>some days).py
fig = plt.figure()
a=fig.add_subplot(1,3,1)
my_map = Basemap(projection='merc', lat_0 = 45, lon_0 = -63,
    resolution = 'h', area_thresh = 0.3,
    llcrnrlon=-68, llcrnrlat=42.0,
    urcrnrlon=-59, urcrnrlat=48) 
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'coral')
my_map.drawmapboundary() 
x,y=my_map(df_getfsrs['Longitude'].values,df_getfsrs['Latitude'].values)
my_map.plot(x, y, 'bo', markersize=4)
a.set_title('All sites with raw data',fontsize=10)
my_map.drawparallels(np.arange(40,80,3),labels=[1,0,0,0])
my_map.drawmeridians(np.arange(-180,180,3),labels=[1,1,0,1])
a=fig.add_subplot(1,3,2)
my_map = Basemap(projection='merc', lat_0 = 45, lon_0 = -63,
    resolution = 'h', area_thresh = 0.3,
    llcrnrlon=-68, llcrnrlat=42.0,
    urcrnrlon=-59, urcrnrlat=48) 
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'coral')
my_map.drawmapboundary() 
x,y=my_map(df_fsrs['Longitude'].values,df_fsrs['Latitude'].values)
my_map.plot(x, y, 'bo', markersize=4)
a.set_title('Longterm sites (>1 year)',fontsize=10)
my_map.drawparallels(np.arange(40,80,3),labels=[0,0,0,1])
my_map.drawmeridians(np.arange(-180,180,3),labels=[1,1,0,1])
plt.savefig(save_dir+'compare_getfsrs_map(all sites,>1 year)',dpi=200) 
plt.show()
a=fig.add_subplot(1,3,3)
my_map = Basemap(projection='merc', lat_0 = 45, lon_0 = -63,
    resolution = 'h', area_thresh = 0.3,
    llcrnrlon=-68, llcrnrlat=42.0,
    urcrnrlon=-59, urcrnrlat=48) 
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'coral')
my_map.drawmapboundary()
x,y=my_map(df_fsrs_1000['Longitude'].values,df_fsrs_1000['Latitude'].values)
my_map.plot(x, y, 'bo', markersize=4)
a.set_title('Longterm sites (>1000 days)',fontsize=10)
my_map.drawparallels(np.arange(40,80,3),labels=[0,0,0,1])
my_map.drawmeridians(np.arange(-180,180,3),labels=[1,1,0,1])
plt.savefig(save_dir+'compare_getfsrs_map(all sites,>1 year,> 1000 days)',dpi=200) 
plt.show()

