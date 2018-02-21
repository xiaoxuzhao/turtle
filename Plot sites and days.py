
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:04:54 2018
@author: xiaoxu
Plot sites and days
"""
from pandas import read_csv
import matplotlib.pyplot as plt
######################
#HRADCODES
day=1000    
input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
save_dir='/home/zdong/xiaoxu/FSRS/figure/'
######################
df_fsrs=read_csv(input_dir+'fsrs_sites(>1 km,year).csv')  #fsrs_sites(>1 km,year).py
df=read_csv(input_dir+'merge_date.csv')       #merge_fsrs.py
df=df.drop_duplicates('Date')
df.to_csv(input_dir+'sort_the_same_date.csv')
df=read_csv(input_dir+'sort_the_same_date.csv')
###################
#get xlim
index_first=list(df.icol(1))
indexs=list(set(index_first))
indexs.sort(key=index_first.index)
###################
days,m,p=[],[],[]
for s in range(len(indexs)):
    a=0
    for i in range(len(index_first)):
          if index_first[i]==indexs[s]:
              a+=1
    if (a>day):
        m.append(a)
        p.append(indexs[s])
    days.append(a)
fig = plt.figure(figsize=(40,5))
a=fig.add_subplot(1,1,1)
plt.bar(indexs,days,0.01,color='green')
plt.title("the sites total days",fontsize=13)
plt.ylabel('Total days')
plt.savefig(save_dir+"All_sites_total_days.png")
fig = plt.figure()
a=fig.add_subplot(1,1,1)
plt.bar(p,m,8,color='green')
plt.title("the sites which days more than " +str(day)+ " days",fontsize=13)
plt.xlabel('Site')
plt.xticks(p,fontsize=10)
plt.ylabel('Total days')
plt.savefig(save_dir+"more_than_"+str(day)+"_days.png")
plt.show()

            

       