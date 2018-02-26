import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
from scipy import interpolate
from pandas import DataFrame
input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
save_dir='/home/zdong/xiaoxu/FSRS/figure/'
#input_dir='/net/data5/jmanning/cts/'
FNMeta=input_dir+'CTSeventList_4589.txt' #1.3MB
"""
Station Details-Q4589
Query,Event_Spec,Event_ID,Cruise,Inst.,Model,Serial,Latitude,Longitude,Start,End,Min_Obs_Dep,Max_Obs_Dep,Sounding,Sampling,Update_Date,Area,Parameter
4589,MTR_BCD2008603_1450_3106_3600_FALL,10652,BCD2008603,MINILOG,Minilog-T,3106,43.4565,-65.4408,24/11/2008,03/01/2009,7.3,14.6,-99,3600,01/03/2012,RECT1,T
4589,MTR_BCD2008603_1468_6523_3600_FALL,10656,BCD2008603,MINILOG,Minilog-T,6523,43.4704,-65.7623,24/11/2008,30/05/2009,82.3,89.6,-99,3600,01/03/2012,RECT1,T
4589,MTR_BCD2008603_1503_4622_3600_FALL,10662,BCD2008603,MINILOG,Minilog-T,4622,45.5437,-64.8938,16/10/2008,24/11/2008,34.7,49.4,-99,3600,01/03/2012,RECT1,T
4589,MTR_BCD2009603_1458_4245_3600_FALL,10722,BCD2009603,MINILOG,Minilog-T,4245,44.5123,-64.0215,30/11/2009,11/03/2010,11,13.7,-99,3600,26/03/2012,RECT1,T
4589,MTR_BCD2009603_1460_4159_3600_FALL,10723,BCD2009603,MINILOG,Minilog-T,4159,43.3167,-65.8,30/11/2009,19/01/2010,21.9,45.7,-99,3600,26/03/2012,RECT1,T
"""
NAMES=['Query','Event_Spec','Event_ID','Cruise','Instr','Model','Serial','Latitude','Longitude','Start','End','Min_Obs_Dep','Max_Obs_Dep','Sounding','Sampling','Update_Date','Area','Parameter']
DMeta=np.genfromtxt(FNMeta,skip_header=2,delimiter=',',dtype=None,names=NAMES)

#len(DMeta['Latitude']) # 8545

lat=DMeta['Latitude']
lon=DMeta['Longitude']
#lat=np.array(DMeta['Latitude']) # convert to np.array for vector processing
#lon=np.array(DMeta['Longitude'])

t0=datetime(2000,1,1)
TIMESTAMP=DMeta['Start']
t = np.array([datetime.strptime(TIMESTAMP[k],'%d/%m/%Y') for k in range(len(TIMESTAMP)) ])
ty=np.array([(t[k]-t0).total_seconds() for k in range(len(t))])/(365.25*24*60*60)+2000.
ty_start=ty

TIMESTAMP=DMeta['End']
t = np.array([datetime.strptime(TIMESTAMP[k],'%d/%m/%Y') for k in range(len(TIMESTAMP)) ])
ty=np.array([(t[k]-t0).total_seconds() for k in range(len(t))])/(365.25*24*60*60)+2000.
ty_end=ty


# select stations within a rectangle around Nova Scotia
iR=np.argwhere((lon>=-68.)&(lon<=-58.)&(lat>=42.)&(lat<=47.)).flatten()

lat=lat[iR]
lon=lon[iR]
ty_start=ty_start[iR]
ty_end=ty_end[iR]


# Many stations are clustered around lat, lon lines 
# corresponding to the grid 1deglat/60 x 1deglon/60 or 1nmi x 0.7 nmi
# cos(45deg) = 0.70710678118654757

M=60.
# round lat,lon to 1/60 deg grid
#M=12.
lat1=np.round(lat*M)/M
lon1=np.round(lon*M)/M

plt.figure()
plt.plot(lon,lat,'b.')
plt.xlabel('Longitude, deg')
plt.ylabel('Latitude, deg')
plt.savefig(save_dir+'p_cluster_stations_fig1_'+str(M)+'_bins.png')
plt.show()

# randomize lon, lat to make plot and be able to distinguish individual stations
lon2=lon1+(np.random.rand(len(lon1))-0.5)/M/4.
lat2=lat1+(np.random.rand(len(lat1))-0.5)/M/4.

plt.figure()
plt.plot(lon2,lat2,'r.')
plt.xlabel('Longitude, deg')
plt.ylabel('Latitude, deg')
plt.savefig(save_dir+'p_cluster_stations_fig2_'+str(M)+'_bins.png')
plt.show()


import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
mpl.rcParams['legend.fontsize'] = 10
for i in range(len(lat)):
    z = np.arange(ty_start[i], ty_end[i], 1./12)
    x = z*0.+lon2[i]
    y = z*0.+lat2[i]
#    ax.plot(x, y, z,'g-')
    ax.plot(x, y, z)
    #ax.plot(x, y, z, label='parametric curve')
#ax.legend()
plt.savefig(save_dir+'p_cluster_stations_fig3_'+str(M)+'_bins.png')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
mpl.rcParams['legend.fontsize'] = 10
span=[]# span of time at each bin in #years
for i in range(len(lat)):
    span.append(ty_end[i]-ty_start[i])
    z = np.arange(0.,ty_end[i]-ty_start[i], 1./12)
    x = z*0.+lon2[i]
    y = z*0.+lat2[i]
#    ax.plot(x, y, z,'g-')
    ax.plot(x, y, z)
    #ax.plot(x, y, z, label='parametric curve')
#ax.legend()
print span
plt.savefig(save_dir+'p_cluster_stations_fig4_'+str(M)+'_bins.png')# where M=# bins per degree
plt.show()
data={'Latitude':np.array(lat2),
      'Longitude':np.array(lon2),'Span':np.array(span)}
      
frame=DataFrame(data,columns=['Latitude','Longitude','Span'])
frame.to_csv(input_dir+'p_cluster_stations_'+str(M)+'_bins.csv')
FNData='CTSscalarstats_4589.txt' #118.6MB
"""
Source Data-Q4589
Query,Event_Spec,Event_ID,Latitude,Longitude,Start,End,Obs_Dep,Min,Max,Mean,Stdev,Qual_Flag,Units,Parm_Desc,Scalar_ID,Area
4589,MTR_BCD2007603_1410_1423_3600_spring,11011,44.8831,-62.1254,2007-06-03 00:12:51.0,2007-06-03 23:12:51.0,18.3,3.8,4.5,3.96,0.21,1,degrees C,Temperature,962282,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2007-12-14 00:07:20.0,2007-12-14 23:07:20.0,14.6,4.4,5.4,4.86,0.32,1,degrees C,Temperature,962580,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2007-12-17 00:07:20.0,2007-12-17 23:07:20.0,14.6,2.7,4.2,3.57,0.43,1,degrees C,Temperature,962583,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2007-12-18 00:07:20.0,2007-12-18 23:07:20.0,14.6,2.7,3.9,3.15,0.33,1,degrees C,Temperature,962584,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2007-12-23 00:07:20.0,2007-12-23 23:07:20.0,14.6,2.4,3.8,3.09,0.43,1,degrees C,Temperature,962589,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2007-12-26 00:07:20.0,2007-12-26 23:07:20.0,14.6,2.6,3.4,3,0.23,1,degrees C,Temperature,962592,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2007-12-27 00:07:20.0,2007-12-27 23:07:20.0,14.6,2.6,3.4,2.98,0.2,1,degrees C,Temperature,962593,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-01-08 00:07:20.0,2008-01-08 23:07:20.0,14.6,2.3,3,2.67,0.25,1,degrees C,Temperature,962605,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-01-15 00:07:20.0,2008-01-15 23:07:20.0,14.6,2.7,3.2,3.02,0.14,1,degrees C,Temperature,962612,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-01-30 00:07:20.0,2008-01-30 23:07:20.0,14.6,1.9,3,2.3,0.31,1,degrees C,Temperature,962627,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-02-05 00:07:20.0,2008-02-05 23:07:20.0,14.6,1.4,1.5,1.5,0.02,1,degrees C,Temperature,962633,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-02-09 00:07:20.0,2008-02-09 23:07:20.0,14.6,1.6,1.9,1.82,0.09,1,degrees C,Temperature,962637,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-02-14 00:07:20.0,2008-02-14 23:07:20.0,14.6,1.5,1.9,1.65,0.09,1,degrees C,Temperature,962642,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-02-15 00:07:20.0,2008-02-15 23:07:20.0,14.6,1.6,1.9,1.79,0.11,1,degrees C,Temperature,962643,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-02-24 00:07:20.0,2008-02-24 23:07:20.0,14.6,1.8,2,1.87,0.05,1,degrees C,Temperature,962652,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-02-25 00:07:20.0,2008-02-25 23:07:20.0,14.6,1.9,2,1.91,0.03,1,degrees C,Temperature,962653,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-02-26 00:07:20.0,2008-02-26 23:07:20.0,14.6,1.9,2.1,2.03,0.06,1,degrees C,Temperature,962654,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-03-18 00:07:20.0,2008-03-18 23:07:20.0,14.6,2.4,2.8,2.59,0.11,1,degrees C,Temperature,962675,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-03-22 00:07:20.0,2008-03-22 23:07:20.0,14.6,2.2,2.4,2.26,0.08,1,degrees C,Temperature,962679,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-04-05 00:07:20.0,2008-04-05 23:07:20.0,14.6,3,3.1,3.05,0.05,1,degrees C,Temperature,962693,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-04-06 00:07:20.0,2008-04-06 23:07:20.0,14.6,3.1,3.2,3.14,0.05,1,degrees C,Temperature,962694,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-04-23 00:07:20.0,2008-04-23 23:07:20.0,14.6,5.4,5.7,5.43,0.07,1,degrees C,Temperature,962711,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-05-01 00:07:20.0,2008-05-01 23:07:20.0,14.6,6,6.4,6.14,0.14,1,degrees C,Temperature,962719,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-05-09 00:07:20.0,2008-05-09 23:07:20.0,14.6,6.2,6.9,6.64,0.2,1,degrees C,Temperature,962727,RECT1
4589,MTR_BCD2007603_1422_8900_3600_FALL,11016,44.2595,-66.166,2008-05-21 00:07:20.0,2008-05-21 23:07:20.0,14.6,7.6,8,7.73,0.15,1,degrees C,Temperature,962739,RECT1
4589,MTR_BCD2007603_1438_7174_3600_FALL,11022,44.1077,-66.3238,2007-12-14 00:21:36.0,2007-12-14 23:21:36.0,45.7,5.4,6.2,5.87,0.26,1,degrees C,Temperature,963537,RECT1
4589,MTR_BCD2007603_1438_7174_3600_FALL,11022,44.1077,-66.3238,2007-12-24 00:21:36.0,2007-12-24 23:21:36.0,45.7,4,5.1,4.25,0.23,1,degrees C,Temperature,963547,RECT1
4589,MTR_BCD2007603_1438_7174_3600_FALL,11022,44.1077,-66.3238,2008-01-08 00:21:36.0,2008-01-08 23:21:36.0,45.7,3.5,3.9,3.71,0.11,1,degrees C,Temperature,963562,RECT1
"""

