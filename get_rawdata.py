# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:57:51 2017

@author: zdong
"""
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
from turtleModule import str2ndlist
'''
import matplotlib.pyplot as plt
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
color=['g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray']
for i in range(16):
    plt.plot(np.arange(1,10,2),[i]*5,marker='o',linestyle='-',color=color[i],linewidth=2)
plt.show()
'''
weeks=6# the number means how many weeks should plot from the one exact days
for j in range(weeks):# 
    start_time=(datetime(2018,9,5)+timedelta(days=j*7)).strftime('%m-%d-%Y')
    endtime=(datetime(2018,9,5)+timedelta(days=j*7+6)).strftime('%m-%d-%Y')
    data = pd.read_csv('each_data/data(%s~%s).csv'%(start_time,endtime))
    t_id=data['turtle_id']
    time=data['Time']
    lat=data['Lat']
    lon=data['Lon']
    depth=pd.Series(str2ndlist(data['Depth']))
    temp=pd.Series(str2ndlist(data['Temperature']))
    turtle_id,Time,Lat,Lon,Depth,Temperature=[],[],[],[],[],[]
    for i in data.index:
        for j in range(len(depth[i])):
            turtle_id.append(t_id[i])
            Time.append(time[i])
            Lat.append(lat[i])
            Lon.append(lon[i])
            Depth.append(depth[i][j])
            Temperature.append(temp[i][j])
    D=pd.DataFrame()
    D['turtle_id']=pd.Series(turtle_id)
    D['  Time  ']=pd.Series(Time)
    D['    Lat    ']=pd.Series(Lat)
    D['    Lon    ']=pd.Series(Lon)
    D['Depth(m)']=pd.Series(Depth)
    D['Temperature(°C)']=pd.Series(Temperature)
    D.to_csv('seperated_rawdata/rawdata(%s~%s).csv'%(start_time,endtime))

