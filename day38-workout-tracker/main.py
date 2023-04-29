import requests
import os
import datetime

SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')
SHEETY_AUTH_TOKEN = os.getenv('SHEETY_AUTH_TOKEN')
NUTRITIONIX_APP_ID = os.getenv('NUTRITIONIX_APP_ID')
NUTRITIONIX_APP_KEY = os.getenv('NUTRITIONIX_APP_KEY')
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_query = input('Tell me what exercises you did: ')
age = int(input('What is your age? '))
gender = input('What is your gender? ')
height_cm = float(input('What is your height in ft? ')) * 30.48
weight_kg = float(input('What is your weight in lbs? ')) * 0.453592

headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_APP_KEY
}
parameters = {
    'query': exercise_query,
    'gender': gender,
    'weight_kg': weight_kg,
    'height_cm': height_cm,
    'age': age
}
response = requests.post(url=NUTRITIONIX_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
exercise_data = response.json()

date = datetime.datetime.now().strftime('%m/%d/%Y')
time = datetime.datetime.now().strftime('%H:%M:%S')

for exercise in exercise_data['exercises']:
    duration_min = exercise['duration_min']
    calories = exercise['nf_calories']
    name = exercise['name'].title()
    parameters = {
        "workout": {
            'date': date,
            'time': time,
            'exercise': name,
            'duration': duration_min,
            'calories': calories
        }
    }
    headers = {
        'Authorization': f"Bearer {SHEETY_AUTH_TOKEN}"
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=parameters, headers=headers)
    response.raise_for_status()
