# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 15:54:39 2017

@author: zdong
"""
import matplotlib as mpl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from turtleModule import str2ndlist
from datetime import datetime,timedelta
color=['g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','olive','indigo','coral','plum','violet','salmon','tan','navy','maroon','blue','peachpuff','slateblue','khaki','gold','chocolate']
t_ids=[118905,151558,149443,161445,151561,159796,151560,161868,159797,161444,161300,161292,161442,161294,161441,172180,172177,172178,172182,172183,172184,172185,172186,172187,172189,172190,172192,172193,172196,172194]

data = pd.read_csv('position_data(05-05-2017~09-11-2018).csv')
time =  pd.Series((datetime.strptime(x, '%m/%d/%Y %H:%M') for x in data['Time']))
#time=data['Time']
temp=pd.Series(str2ndlist(data['Temperature']))
t_id=data['turtle_id']
ids=t_id.unique()#118905 # this is the interest turtle id
print ids

fig=plt.figure()
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)
for j in range(len(ids)):
    indx=[]  
    for i in data.index:
        if t_id[i]==ids[j]:   
            indx.append(i)
    Time = time[indx]
    Temp = temp[indx]
    surf_temp=[]
    bottom_temp=[]
    for i in Time.index:
        surf_temp.append(Temp[i][0])
        bottom_temp.append(Temp[i][-1])
    for i in range(len(t_ids)): 
        if ids[j]==t_ids[i]:
           ax1.plot(Time, surf_temp,linestyle='-',color=color[i],label='id:'+str(ids[j])) 
           ax2.plot(Time, bottom_temp,linestyle='-',linewidth=0.5,color=color[i],label='id:'+str(ids[j])) 
plt.ylim([7,32])
ax1.set_ylim([7,32])
ax1.set_title('surface',fontsize=10)
ax2.set_title('bottom',fontsize=10)
dates = mpl.dates.drange(np.amin(time), np.max(time), timedelta(days=30))
dateFmt = mpl.dates.DateFormatter('%m/%d')#%b
ax1.set_xticklabels(dates, rotation=90,fontsize=8)
ax1.xaxis.set_major_formatter(dateFmt)
ax2.set_xticks(dates)
ax2.set_xticklabels(dates, rotation=90,fontsize=8)
ax2.xaxis.set_major_formatter(dateFmt)
#fig.text(0.5, 0.5, 'Time(2017-2018)', ha='center', va='center', fontsize=10)#  0.5 ,0.04 represent the  plotting scale of x_axis and y_axis
fig.text(0.06, 0.5, 'Temperature('+u'°C)', ha='center', va='center',rotation='vertical',fontsize=14)
plt.savefig('surfaceVSbottom_temp.png',dpi=200)        
plt.show()