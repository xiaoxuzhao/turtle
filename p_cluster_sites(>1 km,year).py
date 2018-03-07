# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 13:23:47 2018

@author: xiaoxu
"""
from pandas import read_csv
import math
from dateutil.parser import parse
from datetime import datetime
import operator
import pandas as pd
import datetime
###############
#HARDCODES
input_dir="/home/zdong/xiaoxu/FSRS/all_files/"
###############
df=read_csv(input_dir+'p_cluster_stations_60.0_bins(fsrs).csv')
lat=df['Latitude']   #get the column of latitude
lon=df['Longitude']  #get the column of longitude
Start=df['Start']    #get the column of start
End=df['End'] 
#latitude 1° ≈ 69 miles longitude varies:
#1° longitude = cosine (latitude) * length of degree (miles) at equator.
la_d=1.00000000/69.00000000
num,indexs,num_row_near,min_start_time,max_end_time,start,end=[],[],[],[],[],[],[]
i=0
lo_d=1/(math.radians(lat[i])*69)
for s in range(len(lat)):
    if lon[i]-lo_d<=lon[s]<=lon[i]+lo_d and lat[i]-la_d<=lat[s]<=lat[i]+la_d:
            num.append(s)
num_row_near.append(len(num))    #get the total num of indexs
indexs.append (num)
for d in range(len(num)):
    T=Start[num[d]]
    T_datetime=parse(T)
    E=End[num[d]]
    E_datetime=parse(E)
    start.append(T_datetime)
    end.append(E_datetime)
start.sort()
end.sort(reverse=True)
mintime=start[0]
maxtime=end[0]  
min_start_time.append(mintime)
max_end_time.append(maxtime) 
for i in range(1,len(Start)):
    I= reduce(operator.concat, indexs)   #make a big list
    if i not in I:
        if s not in I:
           print i
           lo_d=1/(math.radians(lat[i])*69)
           num=[]
           for s in range(0,len(Start)):    #compare points about distances
                if lon[i]-lo_d<=lon[s]<=lon[i]+lo_d and lat[i]-la_d<=lat[s]<=lat[i]+la_d:
                     num.append(s)    #get index of the points which within one kilometer
           num_row_near.append(len(num))    #get the total num of indexs
           indexs.append (num)
    else:
        indexs.append([5000])
        num_row_near.append(1)
    start=[]
    end=[]
    if len(num) is not 0:
         for d in range(len(num)):
             T=Start[num[d]]
             T_datetime=parse(T)
             E=End[num[d]]
             E_datetime=parse(E)
             start.append(T_datetime)
             end.append(E_datetime)
         start.sort()
         end.sort(reverse=True)
         mintime=start[0]
         maxtime=end[0]  
    else:
        mintime=Start[i]
        maxtime=End[i]
    min_start_time.append(mintime)
    max_end_time.append(maxtime)        
min_start_time=pd.Series( min_start_time)
df['min_start_time'] = min_start_time
max_end_time=pd.Series( max_end_time)
df['max_end_time'] = max_end_time
num_row_near= pd.Series(num_row_near)
df['num_row_near'] = num_row_near
indexs=pd.Series(indexs)
df['indexs'] = indexs
for i in range(0,len(Start)):
    if max_end_time[i]-min_start_time[i]<datetime.timedelta(365,0,0):
        df.drop(i, inplace=True)
df=df.dropna()  # remove blank rows 
for i in df.index:
        if indexs[i]==([5000]):
             df.drop(i, inplace=True)        
print df
df.to_csv(input_dir+'p_cluster_sites(>1 km,year).csv')
    
