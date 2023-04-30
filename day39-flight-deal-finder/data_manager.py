import requests
import os


class DataManager:
    def __init__(self):
        self.auth_token = os.getenv('SHEETY_AUTH_TOKEN')
        self.endpoint = os.getenv('SHEETY_ENDPOINT')

    def get_rows(self):
        headers = {
            'Authorization': f"Bearer {self.auth_token}"
        }
        response = requests.get(url=self.endpoint, headers=headers)
        response.raise_for_status()
        return response.json()['prices']
