import datetime as dt
import random
import smtplib
import os

weekday = dt.datetime.now().weekday()

if weekday == 2:  # Only on Wednesday
    with open('quotes.txt', 'r') as quotes_file:
        lines = quotes_file.readlines()
    quote = random.choice(lines)

    my_email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))

    with smtplib.SMTP(smtp_server, port=smtp_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Weekly Motivation Quote\n\n{quote}")




