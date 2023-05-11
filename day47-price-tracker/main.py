import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
import os

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:112.0) Gecko/20100101 Firefox/112.0',
    'Accept-Language': 'en-US,en;q=0.5'
}
response = requests.get(AMAZON_URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

div_element = soup.select_one(selector="#corePrice_feature_div")
price_str = div_element.select_one(selector=".a-offscreen").getText()
price = float(price_str[1:])

if price < 100:
    product_name = soup.title.string.split(":")[1]
    alert_message = f"Subject:Price Alert - Instant Pot ${price:0.2f}\n\n" \
                    + product_name.strip() + "\n\n" + f"Price is now ${price:0.2f}!\n\n" \
                    + AMAZON_URL
    with SMTP(SMTP_SERVER, port=SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL_ADDRESS, to_addrs=EMAIL_ADDRESS,
                            msg=alert_message.encode("utf-8"))
