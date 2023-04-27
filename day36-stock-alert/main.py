import requests
import os
import datetime
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_ENDPOINT = "https://www.alphavantage.co/query"
AV_API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL_ADDRESS = os.getenv("TO_EMAIL_ADDRESS")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")


def get_stock_data():
    parameters = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': STOCK,
        'apikey': AV_API_KEY
    }
    response = requests.get(AV_ENDPOINT, params=parameters)
    response.raise_for_status()
    return response.json()


def get_percent_change(data):
    today_date = datetime.datetime.now()
    yesterday_date = (today_date - datetime.timedelta(days=1))
    two_days_ago_date = (today_date - datetime.timedelta(days=2))
    yesterday_date_str = yesterday_date.strftime('%Y-%m-%d')
    two_days_ago_str = two_days_ago_date.strftime('%Y-%m-%d')
    price_yesterday = float(data['Time Series (Daily)'][yesterday_date_str]['4. close'])
    price_two_days_ago = float(data['Time Series (Daily)'][two_days_ago_str]['4. close'])
    return (price_yesterday - price_two_days_ago) / price_two_days_ago * 100


def get_news_data():
    parameters = {
        'apiKey': NEWS_API_KEY,
        'q': COMPANY_NAME
    }
    response = requests.get(NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()
    return response.json()


def send_email(message_str):
    with smtplib.SMTP(SMTP_SERVER, port=int(SMTP_PORT)) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL_ADDRESS,
                            to_addrs=TO_EMAIL_ADDRESS, msg=message_str)


if __name__ == '__main__':
    stock_data = get_stock_data()
    percent_change = get_percent_change(stock_data)

    if abs(percent_change) >= 5:
        news_data = get_news_data()
        total_results = int(news_data['totalResults'])
        for article_index in range(min(3, total_results)):
            article_title = news_data['articles'][article_index]['title']
            article_url = news_data['articles'][article_index]['url']
            symbol = "🔻" if percent_change < 0 else "🔺"
            send_email((f"Subject:{STOCK} {symbol}{abs(percent_change):.0f}%\n\n"
                       + f"Headline: {article_title}\nURL: {article_url}").encode("utf-8"))
