# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 12:29:21 2018

@author: xiaoxu
"""

import numpy as np
from pandas import read_csv
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
from scipy import interpolate
from pandas import DataFrame
input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
save_dir='/home/zdong/xiaoxu/FSRS/figure/'
FNMeta=read_csv(input_dir+'getfsrs.csv')
lat=FNMeta['Latitude']
lon=FNMeta['Longitude']
event_spec=FNMeta['Event_Spec']
start=FNMeta['Start']
end=FNMeta['End']
t0=datetime(2000,1,1)
TIMESTAMP=FNMeta['Start']
t = np.array([datetime.strptime(TIMESTAMP[k],'%d/%m/%Y') for k in range(len(TIMESTAMP)) ])
ty=np.array([(t[k]-t0).total_seconds() for k in range(len(t))])/(365.25*24*60*60)+2000.
ty_start=ty

TIMESTAMP=FNMeta['End']
t = np.array([datetime.strptime(TIMESTAMP[k],'%d/%m/%Y') for k in range(len(TIMESTAMP)) ])
ty=np.array([(t[k]-t0).total_seconds() for k in range(len(t))])/(365.25*24*60*60)+2000.
ty_end=ty
"""
iR=np.argwhere((lon>=-68.)&(lon<=-58.)&(lat>=42.)&(lat<=47.)).flatten()

lat=lat[iR]
lon=lon[iR]
ty_start=ty_start[iR]
ty_end=ty_end[iR]
"""
M=60.
lat1=np.round(lat*M)/M
lon1=np.round(lon*M)/M
# randomize lon, lat to make plot and be able to distinguish individual stations
lon2=lon1+(np.random.rand(len(lon1))-0.5)/M/4.
lat2=lat1+(np.random.rand(len(lat1))-0.5)/M/4.
span=[]# span of time at each bin in #years
for i in range(len(lat)):
    span.append(ty_end[i]-ty_start[i])
data={'Event_Spec':np.array(event_spec),
      'Latitude':np.array(lat2),
      'Longitude':np.array(lon2),
      'Start':np.array(start),
      'End':np.array(end),
      'Span':np.array(span)}     
frame=DataFrame(data,columns=['Event_Spec','Latitude','Longitude','Start','End','Span'])
frame.to_csv(input_dir+'p_cluster_stations_'+str(M)+'_bins(fsrs).csv')



