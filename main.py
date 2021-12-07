from flask import Flask


from app.routes.WeatherStats import WeatherStats

application = Flask(__name__)
WeatherStats.register(application)


if __name__ == '__main__':
    application.run(debug=True,port=5001,host='127.0.0.1')






