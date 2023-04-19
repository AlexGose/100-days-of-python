import pandas as pd
import datetime as dt
import random
import smtplib
import os


def birthdays_today():
    birthday_data = pd.read_csv('birthdays.csv')
    now = dt.datetime.now()
    month = now.month
    day = now.day
    return birthday_data[(birthday_data['month'] == month) & (birthday_data['day'] == day)]


def send_email(address, message):
    my_email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))

    with smtplib.SMTP(smtp_server, port=smtp_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=address,
                            msg=f"Subject:Happy Birthday!\n\n{message}")


if __name__ == '__main__':
    birthday_people = birthdays_today()

    for index in birthday_people.index:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", 'r') as letter_file:
            letter_content = letter_file.read()
        letter_content = letter_content.replace('[NAME]',
                                                birthday_people['name'].loc[index])

        send_email(birthday_people['email'].loc[index], letter_content)
