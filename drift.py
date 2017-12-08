## -*- coding: utf-8 -*-
"""
Created on  Dec 5 12:33 2017
@author: xiaoxu
"""
import gspread
from geopy.geocoders import Nominatim
from oauth2client.service_account import ServiceAccountCredentials
from bokeh.io import output_file, show
from bokeh.models import (GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool, HoverTool, ResetTool)
import bokeh.plotting as bk
from collections import OrderedDict

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('python sheets-c128999af063.json', scope)   # you have to change the json filename to your downloaded file
gc = gspread.authorize(credentials)  #get the credentials
sheet = gc.open("drifter").sheet1    #the google sheet name

#######################change the googlesheets
"""
whole_values=sheet.get_all_values()  #get the whole values
first_col = sheet.col_values(1)      #get the whole first column values

sheet.update_cell(1,1,"name")        #change the special cell
sheet.update_cell(1,4,"lon")         #change the special cell
sheet.update_cell(1,5,"lat")         #change the special cell
row=["jasper","Maspee","Ma"]
index=1
sheet.insert_row(row,index)          #insert a row
sheet.delete_row(1)                  #delete a row
row_counts=sheet.row_count          #find out the total number of rows
"""
row_counts=4
for i in range(row_counts):
     lat=[]
     lon=[]
     town=sheet.col_values(2)[i+1]
     state=sheet.col_values(3)[i+1]
    
     geolocator = Nominatim()
     address="%s,%s"% (town,state)             #get the town,state from googlesheets
     location = geolocator.geocode(address,timeout=10)
     if location:
         lat=location.latitude          #get the latitude
         lon=location.longitude         #get the longitude
     else :
         lat = None
         lon = None
     D="D%s"%(i+2)
     E="E%s"%(i+2)
     sheet.update_acell(D,lat)        #put the latitude in the googlesheets
     sheet.update_acell(E,lon)        #put the longitude in the googlesheets
col_lat = sheet.col_values(4)[1:row_counts+1] #]    get the whole column values
col_lon= sheet.col_values(5)[1:row_counts+1] #]    get the whole column values
names=sheet.col_values(1)[1:row_counts+1]
towns=sheet.col_values(2)[1:row_counts+1]
states=sheet.col_values(3)[1:row_counts+1]            
map_options = GMapOptions(lat=41.6688, lng=-70.2962, map_type="roadmap", zoom=8)# satellite, roadmap, terrain or hybrid
plot = GMapPlot(plot_width=1150, plot_height=570,x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options)
plot.title.text = "Drifter finders map"
plot.title.text_font_size = "25px"
plot.api_key = "AIzaSyCv-fr0_kxOGE0Qe0bygKVvG064rV-Hrps "
source = ColumnDataSource(data=dict(lat=col_lat,lon=col_lon,name=names,town=towns,state=states))
circle = Circle(x="lon", y="lat", size=20, fill_color="blue", fill_alpha=0.8, line_color="red")
plot.add_glyph(source, circle)
plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool(), HoverTool(), ResetTool())
output_file("Drifter finders map.html")
hover = plot.select(dict(type=HoverTool))

hover.tooltips = OrderedDict([("name","@name"),("town","@town"),("state","@state")])
show(plot)
      
      
