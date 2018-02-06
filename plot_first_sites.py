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
index_sites=df["index_sites"]
index_sites=list(index_sites)
index = list(set(index_sites))
index.sort(key=index_sites.index)
first_appear=[]
for i in range(len(index)):
      q=index_sites.index(index[i])
      first_appear.append(q)
print first_appear,index
Date=[]
for i in date:
    Date.append(parser.parse(i[0:10]))
fig = plt.figure(figsize=(10,5))
s,a,d,f,g,h,j,k,l,p=0,0,0,0,0,0,0,0,0,0
dep1,dep2,dep3,dep4,dep5,dep6,dep7,dep8,dep9,dep10=0,0,0,0,0,0,0,0,0,0
for i in range(len(date)):
    if index_sites[i]==index[0]:
         s+=1
         dep1+=depth[i]
    elif index_sites[i]==index[1]:
         a+=1
         dep2+=depth[i]
    elif index_sites[i]==index[2]:
         d+=1
         dep3+=depth[i]
    elif index_sites[i]==index[3]:
         f+=1
         dep4+=depth[i]
    elif index_sites[i]==index[4]:
         g+=1
         dep5+=depth[i]
    elif index_sites[i]==index[5]:
          h+=1
          dep6+=depth[i]
    elif index_sites[i]==index[6]:
          j+=1
          dep7+=depth[i]
    elif index_sites[i]==index[7]:
          k+=1
          dep8+=depth[i]
    elif index_sites[i]==index[8]:
          l+=1
          dep9+=depth[i]
    elif index_sites[i]==index[9]:
          p+=1
          dep10+=depth[i]
dep_1=int(round(dep1/s))
dep_2=int(round(dep2/a))
dep_3=int(round(dep3/d))
dep_4=int(round(dep4/f))
dep_5=int(round(dep5/g))
dep_6=int(round(dep6/h))
dep_7=int(round(dep7/j))
dep_8=int(round(dep8/k))
dep_9=int(round(dep9/l))
dep_10=int(round(dep10/p))
plt.plot(Date[first_appear[0]:first_appear[0]+s], Mean_temp[first_appear[0]:first_appear[0]+s],color="pink",linewidth=1.5, linestyle="-",label=dep_1)
plt.plot(Date[first_appear[1]:first_appear[1]+a], Mean_temp[first_appear[1]:a+first_appear[1]],color="orange",linewidth=1.5, linestyle="-",label=dep_2)
plt.plot(Date[first_appear[2]:first_appear[2]+d], Mean_temp[first_appear[2]:first_appear[2]+d],color="brown",linewidth=1.5, linestyle="-",label=dep_3)
plt.plot(Date[first_appear[3]:first_appear[3]+f ], Mean_temp[first_appear[3]:first_appear[3]+f ],color="green",linewidth=1.5, linestyle="-",label=dep_4)
plt.plot(Date[first_appear[4]:first_appear[4]+g ], Mean_temp[first_appear[4]:first_appear[4]+g ],color="black",linewidth=1.5, linestyle="-",label=dep_5)
plt.plot(Date[first_appear[5]:first_appear[5]+h ], Mean_temp[first_appear[5]:first_appear[5]+h  ],color="red",linewidth=1.5, linestyle="-",label=dep_6)
plt.plot(Date[first_appear[6]:first_appear[6]+j  ], Mean_temp[first_appear[6]:first_appear[6]+j  ],color="blue",linewidth=1.5, linestyle="-",label=dep_7)
plt.plot(Date[first_appear[7]:first_appear[7]+k ], Mean_temp[first_appear[7]:first_appear[7]+k  ],color="yellow",linewidth=1.5, linestyle="-",label=dep_8)
plt.plot(Date[first_appear[8]:first_appear[8]+l  ], Mean_temp[first_appear[8]:first_appear[8]+l ],color="purple",linewidth=1.5, linestyle="-",label=dep_9)
plt.plot(Date[first_appear[9]:first_appear[9]+p ], Mean_temp[first_appear[9]:first_appear[9]+p ],color="cyan",linewidth=1.5, linestyle="-",label=dep_10)
plt.legend(loc='upper left',bbox_to_anchor=(0, 1.0),ncol=4,title="Mean depth(m)")   
plt.title("the site 0 within 1 kilometer in the coordinates of 43.4503,-65.4467 ")
plt.ylim(0,10)
plt.ylabel(u"Mean temperature (\u2103)")
plt.xlabel('Year')
plt.savefig("temperature.png")
plt.show()
