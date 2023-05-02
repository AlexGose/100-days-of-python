import requests
import os


class DataManager:
    def __init__(self):
        self.prices_endpoint = os.getenv('SHEETY_PRICES_ENDPOINT')
        self.users_endpoint = os.getenv('SHEETY_USERS_ENDPOINT')
        self.headers = {
            'Authorization': f"Bearer {os.getenv('SHEETY_AUTH_TOKEN')}"
        }

    def get_prices_rows(self):
        response = requests.get(url=self.prices_endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()['prices']

    def get_users_rows(self):
        response = requests.get(url=self.users_endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()['users']

    def edit_iata_code(self, row, iata_code):
        row_endpoint = self.prices_endpoint + f"/{row}"
        parameters = {
            'price': {
                'iataCode': iata_code
            }
        }
        response = requests.put(url=row_endpoint, json=parameters, headers=self.headers)
        response.raise_for_status()

    def add_user(self, first_name, last_name, email_address):
        parameters = {
            'user': {
                'firstName': first_name,
                'lastName': last_name,
                'email': email_address
            }
        }
        response = requests.post(url=self.users_endpoint, json=parameters, headers=self.headers)
        response.raise_for_status()

