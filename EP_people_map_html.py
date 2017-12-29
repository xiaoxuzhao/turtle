## -*- coding: utf-8 -*-
"""
Created on  Dec 5 12:33 2017
@author: xiaoxu
"""
import gspread # pip install gspread before running this program
from geopy.geocoders import Nominatim  # pip install geopy before running this program
from oauth2client.service_account import ServiceAccountCredentials     #pip install oauth2client before running this program
from bokeh.io import output_file, show    # pip install bokeh before running this program
from bokeh.models import (GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d,DataRange1d, PanTool, WheelZoomTool, CrosshairTool, HoverTool, ResetTool)
from collections import OrderedDict
#get the Google APIs Console,You can refer to the following website:https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('python sheets-c128999af063.json', scope)    # you have to change the json filename to your downloaded file
gc = gspread.authorize(credentials)  #get the credentials
sheet = gc.open("EP_people_MASTER_cs_copy").sheet1     #Deployersthe google sheet name,must send email for xiaoxuzhao2017-gmail-com@python-sheets-188115.iam.gserviceaccount.com
row_counts=2215      #the whole counts of raws in this googlesheets
"""
for i in range(1750,row_counts-1):
    
     City=sheet.col_values(13)[i+1]
     State=sheet.col_values(14)[i+1]
     Country=sheet.col_values(15)[i+1]
     geolocator = Nominatim()
     address="%s,%s,%s"% (City,State,Country)             #get the city,state from googlesheets
     location = geolocator.geocode(address,timeout=50)
     if location:
         lat=location.latitude          #get the latitude
         lon=location.longitude         #get the longitude
     else :
         lat = None
         lon = None
     U="U%s"%(i+2)
     V="V%s"%(i+2)
    
     sheet.update_acell(U,lat)        #put the latitude in the googlesheets
     sheet.update_acell(V,lon)        #put the longitude in the googlesheets
"""

firstname_Miniboat_enthusiast=sheet.col_values(1)[1:row_counts]
lastname_Miniboat_enthusiast=sheet.col_values(2)[1:row_counts]
institution_Miniboat_enthusiast=sheet.col_values(8)[1:row_counts]
citys_Miniboat_enthusiast=sheet.col_values(13)[1:row_counts]
states_Miniboat_enthusiast=sheet.col_values(14)[1:row_counts]
phone_Miniboat_enthusiast=sheet.col_values(12)[1:row_counts]
email_Miniboat_enthusiast=sheet.col_values(9)[1:row_counts]
lat_Miniboat_enthusiast = sheet.col_values(21)[1:row_counts] #    get the whole latitude values
lon_Miniboat_enthusiast= sheet.col_values(22)[1:row_counts] #    get the whole longtitude values
country_Miniboat_enthusiast=sheet.col_values(15)[1:row_counts]   
map_options = GMapOptions(lat=37.9643, lng=-91.8318, map_type="roadmap", zoom=4)# satellite, roadmap, terrain or hybrid
plot = GMapPlot(plot_width=1400, plot_height=1400,x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options,outline_line_color=None)
plot.title.text = "EP_people"
plot.title.text_font_size = "25px"
plot.api_key = "AIzaSyCv-fr0_kxOGE0Qe0bygKVvG064rV-Hrps "
#source_users=dict(lat_users=lat_users,lon_users=lon_users,firstname_users=firstname_users,lastname_users=lastname_users,city_users=citys_users,state_users=states_users,institution_users=institution_users,phone_users=phone_users,email_users=email_users)
#source_finders=dict(lat_finders=lat_finders,lon_finders=lon_finders,name_finders=name_finders,city_finders=citys_finders,state_finders=states_finders,date_finders=date_finders,phone_finders=phone_finders,email_finders=email_finders)
#source= ColumnDataSource(data=source_users,source_finders)
source = ColumnDataSource(data=dict(lat=lat_Miniboat_enthusiast,lon=lon_Miniboat_enthusiast,firstname=firstname_Miniboat_enthusiast,lastname=lastname_Miniboat_enthusiast,city=citys_Miniboat_enthusiast,state=states_Miniboat_enthusiast,phone=phone_Miniboat_enthusiast,email=email_Miniboat_enthusiast,institution=institution_Miniboat_enthusiast,country=country_Miniboat_enthusiast))

circle = Circle(x="lon", y="lat", size=6, fill_color="blue", fill_alpha=0.8, line_color=None)
plot.add_glyph(source,circle)
plot.add_tools(PanTool(), WheelZoomTool(), HoverTool(), ResetTool())
output_file("EP_people.html")
hover = plot.select(dict(type=HoverTool))
hover.point_policy = "follow_mouse"
hover.tooltips = OrderedDict([("Firstname","@firstname"),("Lastname","@lastname"),("City","@city"),("State","@state"),("Institution","@institution"),("Phone","@phone"),("Email","@email")])
show(plot)
