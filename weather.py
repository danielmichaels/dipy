from utils import datetime_helper
from pprint import pprint
import requests
import logging

logging.basicConfig(level=logging.INFO)


class Weather:
    TOKEN = '48b362375868b94f43172bcb13390ffc'

    def __init__(self, city='perth', country='AU'):
        self.city = city
        self.country = country
        self.url = "http://api.openweathermap.org/data/2.5/weather?q={city}," \
                   "{country}&units=metric&appid={TOKEN}".format(
            city=self.city, country=self.country, TOKEN=Weather.TOKEN)

    def get_data(self):
        """Get the weather data in JSON format."""
        # print(self.url)
        response = requests.get(self.url)
        if response.status_code != 200:
            logging.error("API did not return status code of 200")
        data = response.json()
        return data

    def format(self, data):
        """Parse out wanted weather info.

        :arg data, required from :meth get_data"""
        # pprint(data)
        location = data['name']
        temp = data['main']['temp']
        conditions = [item['description'] for item in data['weather']]
        time = data['dt']
        local_time = datetime_helper(time)
        print(location, temp, time, local_time, conditions)


weather = Weather()
data = weather.get_data()
weather.format(data)
