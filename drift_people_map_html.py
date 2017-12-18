
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
sheet_finders = gc.open("drift_finders").sheet1    #the google sheet name,must send email for xiaoxuzhao2017-gmail-com@python-sheets-188115.iam.gserviceaccount.com
sheet_users = gc.open("drift_users").sheet1
sheet_deployers = gc.open("EP_people_MASTER_cs").sheet1
sheet_Miniboat_enthusiast = gc.open("EP_people_MASTER_cs_copy").sheet1
row_counts_finders=338       #the whole counts of raws in this googlesheets
row_counts_users=267
row_counts_deployers=12
row_counts_Miniboat_enthusiast=2215
"""
##################################below get the latitude and longitude
for i in range(row_counts_finders-1):
     City_finders=sheet_finders.col_values(4)[i+1]
     State_finders=sheet_finders.col_values(5)[i+1]
     
     geolocator = Nominatim()
     address="%s,%s"% (City_finders,State_finders)             #get the city,state from googlesheets
     location = geolocator.geocode(address,timeout=50)
     if location:
         lat=location.latitude          #get the latitude
         lon=location.longitude         #get the longitude
     else :
         lat = None
         lon = None
     I="I%s"%(i+2)
     J="J%s"%(i+2)
     sheet_finders.update_acell(I,lat)        #put the latitude in the googlesheets
     sheet_finders.update_acell(J,lon)        #put the longitude in the googlesheets
for i in range(row_counts_users-1):
     City_users=sheet.col_values(6)[i+1]
     State_users=sheet.col_values(7)[i+1]
     geolocator = Nominatim()
     address="%s,%s"% (City_users,State_users)             #get the city,state from googlesheets
     location = geolocator.geocode(address,timeout=50)
     if location:
         lat=location.latitude          #get the latitude
         lon=location.longitude         #get the longitude
     else :
         lat = None
         lon = None
     O="O%s"%(i+2)
     P="P%s"%(i+2)
     sheet.update_acell(O,lat)        #put the latitude in the googlesheets
     sheet.update_acell(P,lon)        #put the longitude in the googlesheets
for i in range(row_counts_deployers-1):
     City_EP_deployers=sheet.col_values(10)[i+1]
     State_EP_deployers=sheet.col_values(11)[i+1]
     geolocator = Nominatim()
     address="%s,%s"% (City_EP_deployers,State_EP_deployers)             #get the city,state from googlesheets
     location = geolocator.geocode(address,timeout=50)
     if location:
         lat=location.latitude          #get the latitude
         lon=location.longitude         #get the longitude
     else :
         lat = None
         lon = None
     M="M%s"%(i+2)
     N="N%s"%(i+2)
     sheet.update_acell(M,lat)        #put the latitude in the googlesheets
     sheet.update_acell(N,lon)        #put the longitude in the googlesheets
for i in range(row_counts_Miniboat_enthusiast-1):
     City_Miniboat_enthusiast=sheet.col_values(13)[i+1]
     State_Miniboat_enthusiast=sheet.col_values(14)[i+1]
     Country_Miniboat_enthusiast=sheet.col_values(15)[i+1]
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

firstname_finders=sheet_finders.col_values(1)[1:row_counts_finders]
lastname_finders=sheet_finders.col_values(2)[1:row_counts_finders]
date_finders=sheet_finders.col_values(3)[1:row_counts_finders]
citys_finders=sheet_finders.col_values(5)[1:row_counts_finders]
states_finders=sheet_finders.col_values(6)[1:row_counts_finders]
phone_finders=sheet_finders.col_values(8)[1:row_counts_finders]
email_finders=sheet_finders.col_values(9)[1:row_counts_finders]
lat_finders = sheet_finders.col_values(10)[1:row_counts_finders] #    get the whole latitude values
lon_finders= sheet_finders.col_values(11)[1:row_counts_finders] #    get the whole longtitude values


firstname_users=sheet_users.col_values(1)[1:row_counts_users]
lastname_users=sheet_users.col_values(2)[1:row_counts_users]
institution_users=sheet_users.col_values(3)[1:row_counts_users]
citys_users=sheet_users.col_values(6)[1:row_counts_users]
states_users=sheet_users.col_values(7)[1:row_counts_users]
phone_users=sheet_users.col_values(11)[1:row_counts_users]
email_users=sheet_users.col_values(12)[1:row_counts_users]
lat_users = sheet_users.col_values(15)[1:row_counts_users] #    get the whole latitude values
lon_users= sheet_users.col_values(16)[1:row_counts_users] #    get the whole longtitude values

firstname_deployers=sheet_deployers.col_values(1)[1:row_counts_deployers]
lastname_deployers=sheet_deployers.col_values(2)[1:row_counts_deployers]
institution_deployers=sheet_deployers.col_values(5)[1:row_counts_deployers]
citys_deployers=sheet_deployers.col_values(10)[1:row_counts_deployers]
states_deployers=sheet_deployers.col_values(11)[1:row_counts_deployers]
phone_deployers=sheet_deployers.col_values(7)[1:row_counts_deployers]
email_deployers=sheet_deployers.col_values(6)[1:row_counts_deployers]
lat_deployers = sheet_deployers.col_values(13)[1:row_counts_deployers] #    get the whole latitude values
lon_deployers= sheet_deployers.col_values(14)[1:row_counts_deployers] #    get the whole longtitude values



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
    
