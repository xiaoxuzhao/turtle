# routine to read and process the FSRS data (mission # 603-5) from CTS source data download
#
from pandas import read_csv
import sys
from mpl_toolkits.basemap import Basemap
#sys.path.append('/net/home3/ocn/jmanning/py/mygit/modules/basemap') #JiM's toolbox collection location
sys.path.append('/home/zdong/anaconda/lib/python2.7/site-packages/mpl_toolkits/basemap') #Xiaoxu's toolbox collection location
#from basemap_options import basemap_standard as bms #basemap option
import matplotlib.pyplot as plt
from math import radians, cos, sin, atan, sqrt
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2]) 
    #print 34
    dlon = lon2 - lon1  
    dlat = lat2 - lat1  
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2 
    c = 2 * atan(sqrt(a)/sqrt(1-a))  
    r = 6371
    d=c * r
    #print type(d)
    return d
# read one data files
#dfh=read_csv('/net/data5/jmanning/cts/CTSeventList_4589.txt',skiprows=[0])   # loads header (ie metadata)
dfh=read_csv('/home/zdong/xiaoxu/FSRS/CTSeventList_4589.txt',skiprows=[0])     # loads header (ie metadata)
# extract all FSRS deployment sites
dfh=dfh[dfh['Cruise'].str.contains('603|604|605')] #extracts only FSRS codes
n_column= ['Event_Spec','Cruise','Latitude','Longitude','Start','End']
lat=dfh['Latitude']
lon=dfh['Longitude']
dis=[]
for i in range(20):
    for s in range(i+1,20):
        I=haversine(lon[i],lat[i],lon[s],lat[s])
        dis.append(I)
print dis
new_dfh = dfh[n_column]        
new_dfh.to_csv('text.csv')
# plot basemap with all FSRS deployment locations from metadata file
"""
m=bms([42,47],[-68,-59],[1,1])# hardcoded extent of the map
x,y=m(dfh['Longitude'].values,dfh['Latitude'].values) #converts lat/lon to basemap xy-coordinates
m.scatter(x,y,3,marker='o',color='r') # plots red dots
#plt.title('Locations of %s FSRS bottom temperature time series between %s and %s' %\
#        (len(lats),date1,date2),fontsize=12)
plt.title('Locations of %s FSRS bottom temperature time series' %\
        (len(x)),fontsize=12)
"""

