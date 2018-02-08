# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:04:54 2018

@author: xiaoxu
"""
from pandas import read_csv
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
df_fsrs=read_csv('fsrs_sites.csv')
df=read_csv('merge_date.csv')
df=df.drop_duplicates('Date')
df.to_csv('sort_the_same_date.csv')
df=read_csv('sort_the_same_date.csv')
###################
#get xlim
index_first=list(df.icol(1))
indexs=list(set(index_first))
indexs.sort(key=index_first.index)
###################
days=[]
m=[]
p=[]
for s in range(len(indexs)):
    a=0
    for i in range(len(index_first)):
          if index_first[i]==indexs[s]:
              a+=1
    if (a>1000):
        m.append(a)
        p.append(indexs[s])
    days.append(a)
fig = plt.figure(figsize=(40,5))
plt.bar(indexs,days,0.01,color='green')
plt.title("the sites total days",fontsize=13)
#plt.xticks(indexs,fontsize=1)
plt.ylabel('Total days')
plt.savefig("All_sites_total_days.png")
plt.show()
plt.bar(p,m,8,color='green')
plt.title("the sites which days more than 1000 days",fontsize=13)
plt.xlabel('Site')
plt.xticks(p,fontsize=10)
plt.ylabel('Total days')
plt.savefig("more than 1000 days.png")
plt.show()
##################
Lat,Lon=[],[]
lat=df_fsrs["Latitude"]
lon=df_fsrs["Longitude"] 
index_fsrs=list(df_fsrs.icol(0))
for s in range(len(p)):
    for i in range(len(index_fsrs)):
        if index_fsrs[i]==p[s]:
            Lat.append(lat[i])
            Lon.append(lon[i]) 
fig = plt.figure()
a=fig.add_subplot(1,1,1)
my_map = Basemap(projection='lcc', lat_0 = 45, lon_0 = -63,
    resolution = 'h', area_thresh = 0.3,
    llcrnrlon=-68, llcrnrlat=42.0,
    urcrnrlon=-59, urcrnrlat=48)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'coral')
my_map.drawmapboundary()
x,y=my_map(Lon,Lat)
my_map.plot(x, y, 'bo', markersize=6)
a.set_title('the sites which days more than 1000 days',fontsize=15)
my_map.drawparallels(np.arange(40,80,3),labels=[1,0,0,0])
my_map.drawmeridians(np.arange(-180,180,3),labels=[1,1,0,1])
plt.savefig('more than 1000 days map',dpi=200) 
plt.show()
            

       