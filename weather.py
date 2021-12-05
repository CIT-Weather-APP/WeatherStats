"""
Steps
1.Create an account on OpenWeatherMap to generate an API key
2.Access confidential information from windows environment
3.Create an API request from python
4.Inteprete the Data
5.Display Results
"""

import os
import requests #python library for making http requests
from datetime import datetime



api_key = os.environ['current_weather_data']
location = input("Enter the Location: ")

#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
full_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+ location + "&appid=" + api_key

api_link = requests.get(full_api_link)
request_data = api_link.json()

# print(request_data)
if request_data['cod'] == '404':
    print("Invalid City: {} Please check the City Name".format(location))

else:
    city_temperature = ((request_data['main']['temp'])-273.15) #calculate temperature in celcius since its easier to understand
    description = request_data['weather'][0]['description']
    humidity = request_data['main']['humidity']
    wind_speed = request_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %y | %I %M %S %p")
    country = request_data['sys']['country']

    print("------------------------------------------------------------------------")
    print("Weather Statistics for - {} city  in {} || {}".format(location.upper(), country,date_time))
    print("------------------------------------------------------------------------")

    print("Current Temperature is: {:.2f} deg C".format(city_temperature))
    print("Current Weather Description is: ",description)
    print("Current Humidity is:",humidity, "%")
    print("Current Speed of Wind is: ",wind_speed, "kmph")
   