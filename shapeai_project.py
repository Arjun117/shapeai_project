# -*- coding: utf-8 -*-
"""


@author: Arjun S Chandran
"""

import requests

from datetime import datetime

api_key = 'a4ad076ed3ca19d2cac771c076ddaa85'
location = input("Enter the city name: ")

complete_api_link = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp'])-273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %y | %I:%M:S %p")

print("------------------------------------------------------------------")
print("Weather stats for - {} || {}".format(location.upper(), date_time))
print("------------------------------------------------------------------")

print("Current temperature is:{:.2f} deg C".format(temp_city))
print("Current weather desc  :",weather_desc)
print("Current Humidity  :",hmdt,'%')
print("Current wind speed  :",wind_spd,'kmph')

with open("Result.txt","w")as f:
    f.write("Weather stats for - {} || {}".format(location.upper(), date_time)+"\n")
    f.write("Current temperature is:{:.2f} deg C".format(temp_city)+"\n")
    f.write("Current weather desc  :"+weather_desc+"\n")
    f.write("Current Humidity  :"+str(hmdt)+'% \n')
    f.write("Current wind speed  :"+str(wind_spd)+'kmph \n')
    
    


