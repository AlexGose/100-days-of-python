import requests
import os
import datetime
from flight_data import FlightData


class FlightSearch:

    def __init__(self, depart_location):
        self.headers = {
            'apikey': os.getenv('KIWI_API_KEY')
        }
        self.server = os.getenv('KIWI_SERVER')
        self.depart_location = depart_location

    def get_iata(self, city_name):
        """Returns International Air Transport Association code"""
        parameters = {
            'term': city_name,
            'locale': 'en-US'
        }
        endpoint = self.server + "/locations/query"
        response = requests.get(url=endpoint, params=parameters, headers=self.headers)
        response.raise_for_status()
        return response.json()['locations'][0]['code']

    def get_flights(self, destination, max_price, min_stay=5, max_stay=14):
        today = datetime.datetime.now()
        tomorrow = today + datetime.timedelta(days=1)
        six_months_after_tomorrow = tomorrow + datetime.timedelta(days=30 * 6)
        endpoint = self.server + "/v2/search"
        parameters = {
            'curr': 'USD',
            'local': 'us',
            'nights_in_dst_from': min_stay,
            'nights_in_dst_to': max_stay,
            'fly_from': self.depart_location,
            'fly_to': destination,
            'date_from': tomorrow.strftime('%d/%m/%Y'),
            'date_to': six_months_after_tomorrow.strftime('%d/%m/%Y'),
            'price_to': max_price,
            'limit': 10
        }
        response = requests.get(url=endpoint, params=parameters, headers=self.headers)
        response.raise_for_status()
        return response.json()['data']

    def get_cheapest_flight(self, destination, max_price, min_stay=5, max_stay=14):
        flights = self.get_flights(destination, max_price, min_stay=min_stay, max_stay=max_stay)
        if flights:
            return self.get_flights(destination, max_price, min_stay=min_stay, max_stay=max_stay)[0]
        else:
            return flights


if __name__ == '__main__':
    fs = FlightSearch('STN')
    cheapest_flight = fs.get_cheapest_flight('BER', 60)
    fd = FlightData.parse_json(cheapest_flight)
    print(fd)
