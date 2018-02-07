# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 18:56:57 2018

@author: xiaoxu
"""
from dateutil import parser
from pandas import read_csv
import matplotlib.pyplot as plt
df=read_csv('sorted.csv')
index_sites=df["index_sites"]
date=df["Date"]
Mean_temp=df["Mean_temp"]
depth=df["Depth"]
#######################
#[1071, 728, 2844, 2649, 762, 2650, 2076, 0, 2486, 3449] 
#get unique station value in order
index_sites=df["index_sites"]
index_sites=list(index_sites)
index = list(set(index_sites))
index.sort(key=index_sites.index)
#######################
#Get the first occurrence of the index value
first_appear=[]
for i in range(len(index)):
      q=index_sites.index(index[i])
      first_appear.append(q)
####################### 
#Convert date columns to time format,and only need top ten
Date=[]
for i in date:
    Date.append(parser.parse(i[0:10]))
#######################
fig = plt.figure(figsize=(10,5))
color=["pink","orange","brown","green","black","red","blue","yellow","purple","cyan"]
for s in range(len(index)):
     a,dep=0,0
     for i in range(len(date)):
        if index_sites[i]==index[s]:
            a+=1
            dep+=depth[i]
     Depth=int(round(dep/a))
     plt.plot(Date[first_appear[s]:first_appear[s]+a], Mean_temp[first_appear[s]:first_appear[s]+a],color=color[s],linewidth=1.5, linestyle="-",label=Depth)
plt.legend(loc='upper left',bbox_to_anchor=(0, 1.0),ncol=4,title="Mean depth(m)")   
plt.title("the site 0 within 1 kilometer in the coordinates of 43.4503,-65.4467 ")
plt.ylim(0,10)
plt.ylabel(u"Mean temperature (\u2103)")
plt.xlabel('Year')
plt.savefig("temperature.png")
plt.show()


