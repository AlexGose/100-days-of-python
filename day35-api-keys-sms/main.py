import requests
import os
from twilio.rest import Client

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
MY_LATITUDE = os.getenv("MY_LATITUDE")
MY_LONGITUDE = os.getenv("MY_LONGITUDE")

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_FROM")
TWILIO_TO = os.getenv("TWILIO_TO")

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"
parameters = {
    'lat': MY_LATITUDE,
    'lon': MY_LONGITUDE,
    'exclude': 'minutely',
    'appid': WEATHER_API_KEY,
}

response = requests.get(OWM_ENDPOINT, params=parameters)
print(f"The status code is {response.status_code}")
response.raise_for_status()

data = response.json()
data_12_hours = data['hourly'][:12]

weather_ids = [data_12_hours[hour]['weather'][0]['id'] for hour in range(12)]

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for weather_id in weather_ids:
    if weather_id < 700:  # possibility of rain
        message = client.messages \
            .create(
                body="It's going to rain today.  Better bring an umbrella.",
                from_=TWILIO_FROM,
                to=TWILIO_TO
            )

        print(message.status)
        break
