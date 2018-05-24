from requests import get
from datetime import datetime, timedelta
from pprint import pprint
try:
    from json import loads
except ImportError:
    import simplejson as json
    
KEY = "2bd83c197faa4431f12fd38f9302142d"
# 4792867
# http://api.openweathermap.org/data/2.5/forecast?id=4792867&APPID=2bd83c197faa4431f12fd38f9302142d


def get_weather_data(city_id):
    weather_data = get('http://api.openweathermap.org/data/2.5/forecast?id=4792867&APPID=2bd83c197faa4431f12fd38f9302142d'.format(city_id, KEY))
    return weather_data.json()

weather = get_weather_data('4792867')

def rainForecast():
    rain = 0
    x = 0
    while x < 40:
        try:
            rain = rain + (weather['list'][x]['rain']['3h'])
        except:
            rain = rain + 0
        x = x + 1
    return (rain)

rainForecast()
TotalRain = rainForecast()


