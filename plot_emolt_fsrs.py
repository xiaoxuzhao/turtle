# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:45:00 2018
plot eMolt and FSRS
@author: xiaoxu
"""
import pandas as pd
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
def dm2dd(lat,lon):
    """
    convert lat, lon from decimal degrees,minutes to decimal degrees
    """
    (a,b)=divmod(float(lat),100.)   
    aa=int(a)
    bb=float(b)
    lat_value=aa+bb/60.

    if float(lon)<0:
        (c,d)=divmod(abs(float(lon)),100.)
        cc=int(c)
        dd=float(d)
        lon_value=cc+(dd/60.)
        lon_value=-lon_value
    else:
        (c,d)=divmod(float(lon),100.)
        cc=int(c)
        dd=float(d)
        lon_value=cc+(dd/60.)
    return lat_value, -lon_value
################
#HARDCODES
input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
save_dir='/home/zdong/xiaoxu/FSRS/figure/'
po=[-75,39,-58,49]
################
case=''#'_MAB'
df=pd.read_csv(input_dir+'sqldump_sites'+case+'.dat',index_col=2,delim_whitespace=True)
dfh=pd.read_csv(input_dir+'fsrs_sites(>1 km,year).csv')
fig = plt.figure()
a=fig.add_subplot(1,1,1)
# emolt site
Lon,Lat=[],[]
for k in range(len(df)):
    if int(df['MAXD'][k][-4:])-int(df['MIND'][k][-4:])>0:
      la=df['LAT_DDMM'][k]
      lo=df['LON_DDMM'][k]
      [la,lo]=dm2dd(la,lo)
      Lon.append(lo)
      Lat.append(la)
my_map = Basemap(projection='merc',
    resolution = 'h', area_thresh = 0.3,
    llcrnrlon=po[0], llcrnrlat=po[1],
    urcrnrlon=po[2], urcrnrlat=po[3]) 
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'gray')
my_map.drawmapboundary() 
x,y=my_map(Lon,Lat)
my_map.plot(x, y, 'ro', markersize=4)
x,y=my_map(dfh['Longitude'].values,dfh['Latitude'].values)
my_map.plot(x, y, 'go', markersize=4)
label=["eMOLT","FSRS"]
a.legend(label,loc="lower right")
a.set_title('eMOLT sites(>1 year) and FSRS sites(>1 year)',fontsize=15)
my_map.drawparallels(np.arange(30,80,3),labels=[1,0,0,0])
my_map.drawmeridians(np.arange(-180,180,3),labels=[1,1,0,1])
plt.savefig(save_dir+"plot eMolt sites(>1 year) and fsrs sites(>1 year).png")
plt.show()
