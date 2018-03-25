from token import WEATHER_TOKEN
from utils import datetime_helper
from pprint import pprint
import requests
import logging

logging.basicConfig(level=logging.INFO)


class Weather:

    def __init__(self, city='perth', country='AU'):
        self.city = city
        self.country = country
        self.url = "http://api.openweathermap.org/data/2.5/weather?q={city}," \
                   "{country}&units=metric&appid={TOKEN}".format(
            city=self.city, country=self.country, TOKEN=WEATHER_TOKEN)

    def get_data(self):
        """Get the weather data in JSON format."""
        print(self.url)
        response = requests.get(self.url)
        if response.status_code != 200:
            logging.error("API did not return status code of 200")
        data = response.json()
        return data

    def format(self, data):
        """Parse out wanted weather info.

        :arg data, required from :meth get_data"""
        # pprint(data)
        location, cc = data['name'], data['sys']['country']
        temp = data['main']['temp']
        conditions = [item['description'] for item in data['weather']][0]
        time = data['dt']
        local_time = datetime_helper(time)
        output = """
        __**WEATHER REPORT**__\n
        *{0}, {4}*
        Temp:\t **{1}**
        Conditions:\t {2}
        As At:\t **{3}**
        """.format(location, temp, conditions, local_time, cc)
        return output


# weather = Weather()
# data = weather.get_data()
# weather.format(data)
