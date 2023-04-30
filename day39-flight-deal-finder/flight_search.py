import requests
import os


class FlightSearch:

    def __init__(self):
        self.api_key = os.getenv('KIWI_API_KEY')
        self.server = os.getenv('KIWI_SERVER')

    def get_iata(self, city_name):
        """Returns International Air Transport Association code"""
        parameters = {
            'term': city_name,
            'locale': 'en-US'
        }
        headers = {
            'apikey': self.api_key
        }
        endpoint = self.server + "/locations/query"
        response = requests.get(url=endpoint, params=parameters, headers=headers)
        response.raise_for_status()
        return response.json()['locations'][0]['code']
