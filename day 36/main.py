STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_KEY= "VFRCXJ519K8HAQO6"
ALPHAVANTAGE_API_LINK='https://www.alphavantage.co/query'
NWES_API_LINK="https://newsapi.org/v2/everything"

from twilio.rest import Client
import requests
import datetime

stock_parameters={
    'function':'TIME_SERIES_DAILY',
    'symbol'  :STOCK,
    'apikey'  :STOCK_API_KEY
}

news_parameters={
    'apiKey':'810a1eb4aee24963b6701aad5b08b267',
    'qInTitle'      :COMPANY_NAME
}
response_from_alphavantage_website=requests.get(url=ALPHAVANTAGE_API_LINK,params=stock_parameters)
response_from_alphavantage_website.raise_for_status()
daily_stock_data=response_from_alphavantage_website.json()['Time Series (Daily)']

today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
ereyesterday=today-datetime.timedelta(days=2)


yesterday_stock=daily_stock_data[str(yesterday)]
ereyesterday_stock=daily_stock_data[str(ereyesterday)]


yesterday_stock_closing_price=float(yesterday_stock['4. close'])
ereyesterday_stock_closing_price=float(ereyesterday_stock['4. close'])

change_in_stock=format(yesterday_stock_closing_price-ereyesterday_stock_closing_price,".2f")
percentage=abs(float(change_in_stock))/yesterday_stock_closing_price
print(percentage)

if percentage>0.0002:
    response_from_news_website=requests.get(url=NWES_API_LINK,params=news_parameters)
    response_from_news_website.raise_for_status()
    news_data=response_from_news_website.json()['articles'][:3]
    for headline in news_data:
        news_message=f"\nTSLA: 🔺2% Headline:{headline['title']}\nBrief: {headline['description']}\nsource: {headline['source']['name']}"

        account_sid = "AC8b7feb1fbdac7881fcb7a4a33af3bc57"
        auth_token = "e019a744d0bac8cb389ed161d94bee64"
        client = Client(account_sid, auth_token)
        message = client.messages \
                .create(
                body=f"{news_message}",
                from_='+13609001264',
                to='+92 307 5238297'
            )
