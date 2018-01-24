# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 12:57:20 2018
@author: xiaoxu
"""
from pandas import read_csv
import operator
from pandas import DataFrame
import datetime
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
###########
Event_spec1=dfh1["Event_Spec"]
Event_spec3=dfh3["Event_Spec"]
lat=dfh1["Latitude"]
lon=dfh1["Longitude"]
start1=dfh1["Start"]
start3=dfh3["Start"]
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
###########get Event_spec,Latitude,Longitude,Date,Depth,Min_temp,Max_temp,Mean_temp,Stdev_temp,Quality
for i in index_site:
    for s in dfh3.index:
        Event_spec.append(Event_spec1[i])
        Latitude.append(lat[i])
        Longitude.append(lon[i])
        Date.append(start1[i])
        if (Event_spec1[i]==Event_spec3[s]) and (datetime.datetime.strptime(start1[i],"%d/%m/%Y")
           ==datetime.datetime.strptime(start3[s][0:10],"%Y-%m-%d")):
            print s
            Depth.append(Dep[s])
            Min_temp.append(Min_t[s])
            Max_temp.append(Max_t[s])
            Mean_temp.append(Mean_t[s])
            Stdev_temp.append(Stdev_t[s])
            Quality.append(Qual[s])
###########
data={'Event_spec':Event_spec,'Latitude':Latitude,
      'Longitude':Longitude,'Date':Date,'Depth':Depth,
      'Min_temp':Min_temp,'Max_temp':Max_temp,'Mean_temp':Mean_temp,
      'Stdev_temp':Stdev_temp,'index_site':index_site,'Quality':Quality}
frame=DataFrame(data,columns=['index_site','Event_spec','Latitude','Longitude','Date',
                              'Depth','Min_temp','Max_temp','Mean_temp',
                              'Stdev_temp','Quality'],index='index')
frame.to_csv("merge_date.csv")