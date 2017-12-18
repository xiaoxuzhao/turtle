## -*- coding: utf-8 -*-
"""
Created on  Dec 5 12:33 2017
@author: xiaoxu
"""
import gspread # pip install gspread before running this program
from geopy.geocoders import Nominatim  # pip install geopy before running this program
from oauth2client.service_account import ServiceAccountCredentials     #pip install oauth2client before running this program
from bokeh.io import output_file, show    # pip install bokeh before running this program
from bokeh.models import (GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool, HoverTool, ResetTool)
from collections import OrderedDict
#get the Google APIs Console,You can refer to the following website:https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('python sheets-c128999af063.json', scope)    # you have to change the json filename to your downloaded file
gc = gspread.authorize(credentials)  #get the credentials
sheet = gc.open("EP_people_MASTER_cs_copy").sheet1     #Deployersthe google sheet name,must send email for xiaoxuzhao2017-gmail-com@python-sheets-188115.iam.gserviceaccount.com
row_counts=2215      #the whole counts of raws in this googlesheets
for i in range(852,row_counts-1):
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
firstname_Miniboat_enthusiast=sheet_Miniboat_enthusiast.col_values(1)[1:row_counts_Miniboat_enthusiast]
lastname_Miniboat_enthusiast=sheet_Miniboat_enthusiast.col_values(2)[1:row_counts_Miniboat_enthusiast]
institution_Miniboat_enthusiast=sheet_Miniboat_enthusiast.col_values(8)[1:row_counts_Miniboat_enthusiast]
citys_Miniboat_enthusiast=sheet_Miniboat_enthusiast.col_values(13)[1:row_counts_Miniboat_enthusiast]
states_Miniboat_enthusiast=sheet_Miniboat_enthusiast.col_values(14)[1:row_counts_Miniboat_enthusiast]
phone_Miniboat_enthusiast=sheet_Miniboat_enthusiast.col_values(12)[1:row_counts_Miniboat_enthusiast]
email_Miniboat_enthusiast=sheet_Miniboat_enthusiast.col_values(9)[1:row_counts_Miniboat_enthusiast]
lat_Miniboat_enthusiast = sheet_Miniboat_enthusiast.col_values(21)[1:row_counts_Miniboat_enthusiast] #    get the whole latitude values
lon_Miniboat_enthusiast= sheet_Miniboat_enthusiast.col_values(22)[1:row_counts_Miniboat_enthusiast] #    get the whole longtitude values
country_Miniboat_enthusiast=sheet_Miniboat_enthusiast.col_values(15)[1:row_counts_Miniboat_enthusiast]   


map_options = GMapOptions(lat=37.9643, lng=-91.8318, map_type="roadmap", zoom=4)# satellite, roadmap, terrain or hybrid
plot = GMapPlot(plot_width=1150, plot_height=570,x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options)
plot.title.text = "Drift finders(Green),users(Red),deployers(Blue)"
plot.title.text_font_size = "25px"
plot.api_key = "AIzaSyCv-fr0_kxOGE0Qe0bygKVvG064rV-Hrps "
#source_users=dict(lat_users=lat_users,lon_users=lon_users,firstname_users=firstname_users,lastname_users=lastname_users,city_users=citys_users,state_users=states_users,institution_users=institution_users,phone_users=phone_users,email_users=email_users)
#source_finders=dict(lat_finders=lat_finders,lon_finders=lon_finders,name_finders=name_finders,city_finders=citys_finders,state_finders=states_finders,date_finders=date_finders,phone_finders=phone_finders,email_finders=email_finders)
#source= ColumnDataSource(data=source_users,source_finders)
color=[]

date_users=[]
for i in range(row_counts_users-1):
    color.append("red")
    date_users.append(" ")
 
for i in range(row_counts_finders-1):
    color.append("green")
    institution_users.append(" ")

for i in range(row_counts_deployers-1):
    color.append("blue")


lat_users.extend(lat_finders)
lat_users.extend(lat_deployers)

lon_users.extend(lon_finders)
lon_users.extend(lon_deployers)

date_users.extend(date_finders)
firstname_users.extend(firstname_finders)
firstname_users.extend(firstname_deployers)

lastname_users.extend(lastname_finders)
lastname_users.extend(lastname_deployers)

citys_users.extend(citys_finders)
citys_users.extend(citys_deployers)

states_users.extend(states_finders)
states_users.extend(states_deployers)

phone_users.extend(phone_finders)
phone_users.extend(phone_deployers)

email_users.extend(email_finders)
email_users.extend(email_deployers)

institution_users.extend(institution_deployers)

for i in range(row_counts_deployers-1):
    date_users.append(" ")
for i in range(row_counts_Miniboat_enthusiast-1):
    date_users.append(" ")
source = ColumnDataSource(data=dict(color=color,lat=lat_users,lon=lon_users,firstname=firstname_users,lastname=lastname_users,city=citys_users,state=states_users,phone=phone_users,email=email_users,institution=institution_users,date=date_users))    
circle= Circle(x="lon", y="lat", size=8,fill_color="color", fill_alpha=0.8)

plot.add_glyph(source,circle)
plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool(), HoverTool(), ResetTool())
output_file("Drift_map.html")
hover = plot.select(dict(type=HoverTool))
hover.tooltips = OrderedDict([("Firstname","@firstname"),("Lastname","@lastname"),("Date","@date"),("City","@city"),("State","@state"),("Institution","@institution"),("Phone","@phone"),("Email","@email")])
show(plot)
          
      
