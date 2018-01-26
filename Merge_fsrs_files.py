# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 12:57:20 2018
@author: xiaoxu
"""
from pandas import read_csv
import operator
from pandas import DataFrame
import datetime
import numpy as np
def list_of_groups(init_list, childern_list_len):
    list_of_groups = zip(*(iter(init_list),) *childern_list_len) 
    end_list = [list(i) for i in list_of_groups] 
    count = len(init_list) % childern_list_len 
    end_list.append(init_list[-count:]) if count !=0 else end_list 
    return end_list
dfh1=read_csv('CTSeventList_4589.txt',skiprows=[0])
dfh2=read_csv('fsrs_sites.csv')
dfh3=read_csv('CTSscalarstats_4589.txt',skiprows=[0])
########### #get the whole indexs of the gooddate.csv 2127
indexs=dfh2["indexs"]
indexs=list(indexs)
index_site=reduce(operator.concat, indexs)
index_site=index_site.replace("][",", ")
index_site=index_site.replace("[","")
index_site=index_site.replace("]","")
index_site=index_site.replace(",","")
index_site=index_site.split() 
index_site=[int(i) for i in index_site]
index_site=index_site   
###########
Event_spec1=dfh1["Event_Spec"]
Event_spec3=dfh3["Event_Spec"]
lat=dfh1["Latitude"]
lon=dfh1["Longitude"]
start1=dfh1["Start"]
start3=dfh3["Start"]
end3=dfh3["End"]
Dep=dfh3["Obs_Dep"]
Min_t=dfh3["Min"]
Max_t=dfh3["Max"]
Mean_t=dfh3["Mean"]
Stdev_t=dfh3["Stdev"]
Qual=dfh3["Qual_Flag"]
Depth,Min_temp,Max_temp,Mean_temp,Stdev_temp,Event_spec,Latitude,Longitude,Date,Quality=[],[],[],[],[],[],[],[],[],[]
###########get index
site_index=list(dfh2.icol(0))
site_index=list_of_groups(site_index,1) #divide a large list into small lists
num=list(dfh2["num_row_near"])
rows=len(num)
index=[]
for s in range(0,rows):
    for i in site_index[s]:
         for j in range(int(num[s])):
              index.append(i) 
index=index
###########get Event_spec,Latitude,Longitude,Date,Depth,Min_temp,Max_temp,Mean_temp,Stdev_temp,Quality
for i in index_site:
     Event_spec.append(Event_spec1[i])
     Latitude.append(lat[i])
     Longitude.append(lon[i])
     Date.append(start1[i])
     for s in dfh3.index:
        if (Event_spec1[i]==Event_spec3[s]) and (datetime.datetime.strptime(start1[i],"%d/%m/%Y")
           ==datetime.datetime.strptime(start3[s][0:10],"%Y-%m-%d"))and start3[s]!=end3[s]:
              print i,s
              dep=Dep[s]
              min_t=Min_t[s]
              max_t=Max_t[s]
              mean_t=Mean_t[s]
              stdev_t=Stdev_t[s]
              qual=Qual[s]
                 
        else:
               dep=None
               min_t=None
               max_t=None
               mean_t=None
               stdev_t=None
               qual=None   
     Depth.append(dep)
     Min_temp.append(min_t)
     Max_temp.append(max_t)
     Mean_temp.append(mean_t)
     Stdev_temp.append(stdev_t)
     Quality.append(qual)
###########
data={'Event_spec':np.array(Event_spec),'Latitude':np.array(Latitude),
      'Longitude':np.array(Longitude),'Date':np.array(Date),'Depth':np.array(Depth),
      'Min_temp':np.array(Min_temp),'Max_temp':np.array(Max_temp),'Mean_temp':np.array(Mean_temp),
      'Stdev_temp':np.array(Stdev_temp),'index_site':np.array(index_site),'Quality':np.array(Quality)}
frame=DataFrame(data,columns=['index_site','Event_spec','Latitude','Longitude','Date',
                              'Depth','Min_temp','Max_temp','Mean_temp',
                              'Stdev_temp','Quality'],index=index)
frame.to_csv("merge_date.csv")