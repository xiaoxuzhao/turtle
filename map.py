# -*- coding: utf-8 -*-
"""
Created on Thu May  4 13:10:12 2017

@author: zdong
"""
from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
import pandas as pd
from datetime import datetime, timedelta
from turtleModule import draw_basemap
#from gettopo import gettopo
color=['g','darkviolet','orange','b','hotpink','c','peru','lime','brown','orangered','k','magenta','r','cyan','gray','y','pink']
t_ids=[118905,151558,149443,161445,151561,159796,151560,161868,159797,161444,161300,161292,161442,161294,161441,149447,172181]
lonsize = [-76.8, -69.8]
latsize = [34.9, 41.5]
weeks=11# the number means how many weeks should plot from the one exact days
for j in range(weeks):# 
    start_time=(datetime(2018,07,25)+timedelta(days=j*7)).strftime('%m-%d-%Y')
    endtime=(datetime(2018,07,25)+timedelta(days=j*7+6)).strftime('%m-%d-%Y')
    obsData = pd.read_csv('each_data/data(%s~%s).csv'%(start_time,endtime)) # has both observed and modeled profiles
    obsTime =  pd.Series((datetime.strptime(x, '%m/%d/%Y %H:%M') for x in obsData['Time']))
    obsLat=obsData['Lat']
    obsLon=obsData['Lon']
    obsturtle_id=obsData['turtle_id']
    ids=obsturtle_id.unique()#118905 # this is the interest turtle id
    #print ids
    
    waterData=pd.read_csv('tu94_depthbottom.csv')
    wd=waterData['depth_bottom'].dropna()
    Lat=waterData['lat'].dropna()
    Lon=waterData['lon'].dropna()
    
    fig =plt.figure()
    ax = fig.add_subplot(111)
    for j in range(len(ids)):
        indx=[]  # this indx is to get the specifical turtle all index in obsData ,if we use the "where" function ,we just get the length  of tf_index.
        for i in obsData.index:
            if obsturtle_id[i]==ids[j]:   
                indx.append(i)
        Time = obsTime[indx]
        lat = obsLat[indx]
        lon = obsLon[indx]
        for i in range(len(t_ids)): 
            if ids[j]==t_ids[i]:
               plt.plot(lon, lat,linestyle='-',marker='o',markersize=3,linewidth=1,color=color[i],label='id:'+str(ids[j]))  #  
    draw_basemap(fig, ax, lonsize, latsize, interval_lon=2, interval_lat=2)    
    
    lon_is = np.linspace(lonsize[0],lonsize[1],150)
    lat_is = np.linspace(latsize[0],latsize[1],150)  #use for depth line
    depth_i=griddata(np.array(Lon),np.array(Lat),np.array(wd),lon_is,lat_is,interp='linear')
    cs=plt.contour(lon_is, lat_is,depth_i,levels=[100],colors = 'r',linewidths=1,linestyles='--')  #plot 100m depth
    ax.annotate('100m water depth',color='r',fontsize=6,xy=(-73.2089,38.905),xytext=(-73.3034,38.5042),arrowprops=dict(color='red',arrowstyle="->",
                                connectionstyle="arc3"))#xy=(-73.5089,38.505),xytext=(-73.7034,38.0042)
    mintime=obsTime[0].strftime('%m-%d-%Y')
    maxtime=obsTime[len(obsTime)-1].strftime('%m-%d-%Y')
    plt.title('turtle position( '+mintime+'~'+maxtime+' )')#('%s profiles(%s~%s)'% (e,obsTime[0],obsTime[-1]))
    plt.legend(loc='lower right',ncol=2,fontsize = 'xx-small')
    #plt.savefig('turtle_comparison(%s~%s).png'%(mintime,maxtime),dpi=200)
    plt.savefig('map/map(%s~%s).png'%(mintime,maxtime),dpi=200)
    plt.show()

