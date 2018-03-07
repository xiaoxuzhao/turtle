# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:05:54 2018

@author: xiaoxu
"""
from pandas import read_csv
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
###############
#HARDCODES
input_dir="/home/zdong/xiaoxu/FSRS/all_files/"
save_dir="/home/zdong/xiaoxu/FSRS/figure/"
sel="fsrs"#"all"or "fsrs"
#p_cluster_stations_60.0_bins(only)(extracts only FSRS stations 603|604|605)
#p_cluster_stations_60.0_bins(all).csv (all stations)
###############
dfh=read_csv(input_dir+'p_cluster_stations_60.0_bins('+str(sel)+').csv')
dfh=dfh.sort("Span")
dfh.to_csv(input_dir+'sort_p_cluster_stations_60.0_bins('+str(sel)+').csv')
df=read_csv(input_dir+'sort_p_cluster_stations_60.0_bins('+str(sel)+').csv')
span=df["Span"]
lat=df["Latitude"]
lon=df["Longitude"]
indexs=list(df.index)
span_1,lon_1,lat_1=[],[],[]
for i in range(len(span)):
    if span[i]>1:
        span_1.append(span[i])
        lon_1.append(lon[i])
        lat_1.append(lat[i])
fig = plt.figure(figsize=(10,5))
a=fig.add_subplot(1,1,1)
plt.bar(indexs,span,0.01,color='green')
plt.title("the fsrs stations total span",fontsize=13)
plt.ylabel('Span')
plt.savefig(save_dir+"All_stations_span("+str(sel)+").png")
plt.show
fig = plt.figure()
a=fig.add_subplot(1,1,1)
my_map = Basemap(projection='merc', lat_0 = 45, lon_0 = -63,
    resolution = 'h', area_thresh = 0.3,
    llcrnrlon=-68, llcrnrlat=42.0,
    urcrnrlon=-58, urcrnrlat=48) 
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'gray')
my_map.drawmapboundary()
x,y=my_map(lon_1,lat_1)
my_map.plot(x, y, 'ro', markersize=4)
a.set_title('stations span (>1 year)',fontsize=20)
my_map.drawparallels(np.arange(40,80,3),labels=[1,0,0,1])
my_map.drawmeridians(np.arange(-180,180,3),labels=[1,1,0,1])
plt.savefig(save_dir+"plot_stations(>1 year)("+str(sel)+")",dpi=200) 
plt.show()
