"""
Created on Thu Jan 11 11:14:05 2018

@author: xiaoxu
"""
# routine to read and process the FSRS data (mission # 603-5) from CTS source data download
#
from pandas import read_csv
import sys
import pandas as pd
from datetime import datetime
import datetime
import operator
from dateutil.parser import parse
#sys.path.append('/net/home3/ocn/jmanning/py/mygit/modules/basemap') #JiM's toolbox collection location
sys.path.append('/home/zdong/anaconda/lib/python2.7/site-packages/mpl_toolkits/basemap') #Xiaoxu's toolbox collection location
from math import radians, cos, sin, atan, sqrt
##########################
#HARDCODES
input_dir='/home/zdong/xiaoxu/FSRS/'#Xiaoxu's machine
#input_dir='/net/data5/jmanning/cts/'# JiM's machine
#basemap_dir='/home/zdong/anaconda/lib/python2.7/site-packages/mpl_toolkits/basemap'# or '/net/home3/ocn/jmanning/py/mygit/modules/basemap'
maxnumdays=365 # maximum number of days we care about at each site
###########################
def haversine(loni, lati, lons, lats):
       """
       Calculate the great circle distance between two points 
       on the earth (specified in decimal degrees)
       """
       loni, lati, lons, lats = map(radians, [loni, lati, lons, lats]) 
       #print 34
       dlon = lons - loni  
       dlat = lats - lati  
       a = sin(dlat/2)**2 + cos(lati) * cos(lats) * sin(dlon/2)**2 
       c = 2 * atan(sqrt(a)/sqrt(1-a))  
       r = 6371
       d=c * r        
       return d
# read one data files
dfh=read_csv('CTSeventList_4589.txt',skiprows=[0])  # extract all FSRS deployment sites   
dfh=dfh[dfh['Cruise'].str.contains('603|604|605')] #extracts only FSRS codes        
dfh.to_csv('getfsrs.csv')
#dfh=read_csv('/net/data5/jmanning/cts/getfsrs.csv')
dfh=read_csv('getfsrs.csv') #saved and opened the file in order to get fresh index
lat=dfh['Latitude']   #get the column of latitude
lon=dfh['Longitude']  #get the column of longitude
Start=dfh['Start']    #get the column of start
End=dfh['End']        #get the column of end
row_num=len(lat)      #get the  num of whole rows
n_column= ['Event_Spec','Cruise','Latitude','Longitude']      #need this columns form CTSeventList_4589.txt
dfh = dfh[n_column]
i=0
num,indexs,num_row_near,min_start_time,max_end_time=[],[],[],[],[]
for s in range(0,row_num):    #compare points about distances
     if haversine(lon[i],lat[i],lon[s],lat[s])<1:
            num.append(s)    #get index of the points which within one kilometer
num_row_near.append(len(num))    #get the total num of indexs
indexs.append (num)              
start=[]
end=[]
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
for i in range(1,row_num):
    I= reduce(operator.concat, indexs)   #make a big list
    if i not in I:
        if s not in I:
           num=[]
           for s in range(0,row_num):    #compare points about distances
                if haversine(lon[i],lat[i],lon[s],lat[s])<1:
                     num.append(s)    #get index of the points which within one kilometer
           num_row_near.append(len(num))    #get the total num of indexs
           indexs.append (num)
    else:
        print i
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
dfh['min_start_time'] = min_start_time
max_end_time=pd.Series( max_end_time)
dfh['max_end_time'] = max_end_time
num_row_near= pd.Series(num_row_near)
dfh['num_row_near'] = num_row_near
indexs=pd.Series(indexs)
dfh['indexs'] = indexs
for i in range(0,row_num):
    if max_end_time[i]-min_start_time[i]<datetime.timedelta(365,0,0):
        dfh.drop(i, inplace=True)
dfh=dfh.dropna()  # remove blank rows 
for i in dfh.index:
        if indexs[i]==([5000]):
             dfh.drop(i, inplace=True)        
print dfh
dfh.to_csv('fsrs_sites.csv')