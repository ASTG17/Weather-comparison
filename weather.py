#user inputs two cities
#need API to use city names to generate coordinates
#user inputs 2 future dates - max 1 week apart
#each coordinate and day in range given is used with darkweb API
#API pulls real feel daytime temp averages for each date for each city - puts in table?
#plots the temps of each city on the same graph
#also want average precipiation level?
#OR does the 5 year average for city1
#compares with yesterday's weather from city2

import json
import requests

from datetime import datetime#, time
MY_API_KEY = open("darkweb_key.txt").read().strip()
units = "si"
params = {
"units": units
}

venice_coords = [45.4408, 12.3155]
london_coords =[51.5074, -0.1278]

input1 = "29/11/2017" #- after 01/01/1970
input2 = 03/12/2017
date_begin = datetime(2016, 11, 29).isoformat()
#date_end = dt(input2).isoformat()

API_ENDPOINT = "https://api.darksky.net/forecast/"+ MY_API_KEY + "/" + str(venice_coords[0]) + "," + str(venice_coords[1]) + "," + str(date_begin)

numberofyears = 5

results = requests.get(API_ENDPOINT, params)
data = results.json()

#print API_ENDPOINT
time = data["daily"]["data"][0]["time"]
print date_begin
print datetime.fromtimestamp(time)
print data["daily"]["data"][0]["summary"]
print data["daily"]["data"][0]["apparentTemperatureMin"]
print data["daily"]["data"][0]["apparentTemperatureMax"]
