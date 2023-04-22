import requests
from datetime import datetime
import smtplib
import os
import time

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

while True:
    time.sleep(60)
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    coordinates = (iss_latitude, iss_longitude)

    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:

        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now()

        if sunset <= time_now.hour or time_now.hour <= sunrise:
            email_address = os.getenv('EMAIL_ADDRESS')
            email_password = os.getenv('EMAIL_PASSWORD')
            smtp_server = os.getenv('SMTP_SERVER')
            smtp_port = int(os.getenv('SMTP_PORT'))

            with smtplib.SMTP(smtp_server, port=smtp_port) as connection:
                connection.starttls()
                connection.login(user=email_address, password=email_password)
                connection.sendmail(from_addr=email_address,
                                    to_addrs=email_address,
                                    msg=f"The ISS is overhead at the coordinates {coordinates}")
            time.sleep(60 * 60 * 16)  # only send one email
