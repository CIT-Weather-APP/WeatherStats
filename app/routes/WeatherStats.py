
from flask import jsonify
from flask_classy import FlaskView
from flask_classy import route
from flask import Flask,request
import os
import requests #python library for making http requests
from datetime import datetime

"""
Steps
1.Create an account on OpenWeatherMap to generate an API key
2.Access confidential information from windows environment
3.Create an API request from python
4.Inteprete the Data
5.Display Results
"""



class WeatherStats(FlaskView):
    route_base = "/weather/"

 
        
    @route('/fetch_weather_stats',methods=['POST'])
    def fetch_weather_stats(self):
        api_key = os.environ['current_weather_data']
        location = request.args.get('location')
        #api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
        full_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+ location + "&appid=" + api_key

        api_link = requests.get(full_api_link)
        request_data = api_link.json()
     

        if request_data['cod'] == '404':
            print("Invalid City: {} Please check the City Name".format(location))

        else:
            city_temperature = ((request_data['main']['temp'])-273.15) #calculate temperature in celcius since its easier to understand
            description = request_data['weather'][0]['description']
            humidity = request_data['main']['humidity']
            wind_speed = request_data['wind']['speed']
            date_time = datetime.now().strftime("%d %b %y | %I %M %S %p")
            country = request_data['sys']['country']
            data = {
                'City':location,
                'Current Temperature':'{:.2f} deg C'.format(city_temperature),
                'Current Weather Description':description,
                'Current Humidity': str(humidity) + " %",
                'Current Speed of Wind ':str(wind_speed) + " kmph",
                'Country':country,
                'Time':date_time
            }
            return jsonify(data)
