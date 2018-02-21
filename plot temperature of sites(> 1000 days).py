# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:10:37 2018

@author: xiaoxu
"""
#[1, 16, 73, 97, 145, 216, 250, 329, 369, 418]the index of sites which
#days more than 1000 days
from pandas import read_csv
from dateutil import parser
import matplotlib.pyplot as plt
####################
#HAEDCODES
input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
save_dir='/home/zdong/xiaoxu/FSRS/figure/'
s=0
####################
df=read_csv(input_dir+'merge_date.csv')
dfh=read_csv(input_dir+'fsrs_sites(>1000days).csv')
index_1000=list(dfh.icol(0))
index_first=list(df.icol(0))
row_index=[]
for i in range(len(index_first)):
    if index_first[i]==index_1000[s]:
            row_index.append(i)
            p=index_1000[s]
df[row_index[0]:row_index[-1]].to_csv(input_dir+str(p)+"_site_sort.csv", index=False)
df=read_csv(input_dir+str(p)+"_site_sort.csv")
df = df.sort("Date")
index_sites=df["index_sites"]
date=df["Date"]
Mean_temp=df["Mean_temp"]
depth=df["Depth"]
####################### 
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
fig = plt.figure(figsize=(16,5))
color=["pink","orange","brown","green","black","red","blue","yellow","purple","cyan","magenta","chocolate","beige","lime"]
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
plt.ylim(0,15)
plt.ylabel(u"Mean temperature (\u2103)")
plt.xlabel('Year')
plt.savefig(save_dir+str(index_mt3[s])+"site temperature.png")
plt.show()