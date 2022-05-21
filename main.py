
#https://openweathermap.org/forecast5
#https://openweathermap.org/api/geocoding-api
#https://www.weatherbit.io/api/weather-forecast-hourly
#https://www.weatherbit.io/api/swaggerui/weather-api-v2#!/24032hour324732hourly32Forecast/get_forecast_hourly_city_city_country_country

import os
import requests
import json

API_KEY = '05a59ce96cb307a4e12ed503a455c1a0'

def get_lat_lon(country, state, city):
    location_r = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={API_KEY}')

    if(location_r.ok):

        location_info = json.loads(location_r.text)

        #print(location_info)

        lat = (location_info[0]['lat'])
        lon = (location_info[0]['lon'])

        return(lat, lon)

def get_forcast(lat, lon):
    print(lat, lon)
    weather_r = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,hourly,minutely&appid={API_KEY}&units=imperial')

    weather_info = json.loads(weather_r.text)
    
    day1 = weather_info['daily'][0]
    day2 = weather_info['daily'][1]
    day3 = weather_info['daily'][2]
    day4 = weather_info['daily'][3]
    day5 = weather_info['daily'][4]
    #print(day1)
    #print(weather_info)
    
    

print('Welcome to my Awesome weather app!')
country = 'US' #United States
state = str(input('State (ex: KY for Kentucky)\n->')) #ask uiser for state (KY, NY, CA)
city = str(input('City \n->')) #asks user for city (Somerset, Brooklyn, San Francisco)
num_days = 6 #get the 5 day forcast and today


lat, lon = get_lat_lon(country, state, city)
get_forcast(lat, lon)


