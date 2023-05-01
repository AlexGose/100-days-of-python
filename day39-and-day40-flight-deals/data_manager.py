import requests
import os


class DataManager:
    def __init__(self):
        self.endpoint = os.getenv('SHEETY_ENDPOINT')
        self.headers = {
            'Authorization': f"Bearer {os.getenv('SHEETY_AUTH_TOKEN')}"
        }

    def get_rows(self):
        response = requests.get(url=self.endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()['prices']

    def edit_iata_code(self, row, iata_code):
        row_endpoint = self.endpoint + f"/{row}"
        parameters = {
            'price': {
                'iataCode': iata_code
            }
        }
        response = requests.put(url=row_endpoint, json=parameters, headers=self.headers)
        response.raise_for_status()

