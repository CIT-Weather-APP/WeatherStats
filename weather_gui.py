# import required modules
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox
import os


api_key = os.environ['current_weather_data']


#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
full_api_link = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"


# explicit function to get
# weather details
def getweather(city):
    api_link = requests.get(full_api_link.format(city, api_key))
    request_data = api_link.json()

    if request_data:
        city = request_data['name']
        country = request_data['sys']
        temp_kelvin = request_data['main']['temp']
        temp_celsius = temp_kelvin-273.15
        weather1 = request_data['weather'][0]['main']
        final = [city, country, temp_kelvin,
                temp_celsius, weather1]
        return final
    else:
        print("NO Content Found")


# explicit function to
# search city
def search():
	city = city_text.get()
	weather = getweather(city)
	if weather:
		location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
		temperature_label['text'] = str(weather[3])+" Degree Celsius"
		weather_l['text'] = weather[4]
	else:
		messagebox.showerror('Error', "Cannot find {}".format(city))


# Driver Code
# create object
app = Tk()
# add title
app.title("Weather App")
# adjust window size
app.geometry("300x300")

# add labels, buttons and text
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

Search_btn = Button(app, text="Search Weather",
					width=12, command=search)
Search_btn.pack()

location_lbl = Label(app, text="Location", font={'bold', 20})
location_lbl.pack()

temperature_label = Label(app, text="")
temperature_label.pack()
weather_l = Label(app, text="")
weather_l.pack()
app.mainloop()
