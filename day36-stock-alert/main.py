import requests
import os
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_ENDPOINT = "https://www.alphavantage.co/query"
AV_API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')

parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': AV_API_KEY
}
response = requests.get(AV_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

today_date = datetime.datetime.now()
yesterday_date = (today_date - datetime.timedelta(days=1))
two_days_ago_date = (today_date - datetime.timedelta(days=2))
yesterday_date_str = yesterday_date.strftime('%Y-%m-%d')
two_days_ago_str = two_days_ago_date.strftime('%Y-%m-%d')

price_yesterday = float(data['Time Series (Daily)'][yesterday_date_str]['4. close'])
price_two_days_ago = float(data['Time Series (Daily)'][two_days_ago_str]['4. close'])
percent_change = (price_yesterday - price_two_days_ago) / price_two_days_ago * 100
if abs(percent_change) > 5:
    print("Get News")
print(f"{percent_change=}")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

