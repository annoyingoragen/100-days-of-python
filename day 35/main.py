import requests
from twilio.rest import Client
account_sid = "AC8b7feb1fbdac7881fcb7a4a33af3bc57"
auth_token = "e019a744d0bac8cb389ed161d94bee64"
client = Client(account_sid, auth_token)

MY_OPEN_WEATHER_API_KEY="fa8b1937993cc85c1831a88e5d492766"
# LAT=33.565109
# LONG=73.016914
LAT=14.582260
LONG=120.974800
parameters={
    'lat':LAT,
    'lon':LONG,
    'appid':MY_OPEN_WEATHER_API_KEY,
    'exclude':"current,minutely,daily,alerts"
}
open_weather_website_respones=requests.get(url="https://api.openweathermap.org/data/2.5/onecall?",params=parameters)

open_weather_website_respones.raise_for_status()
weather_data=open_weather_website_respones.json()["hourly"][:12]


will_rain=False

for hour_data in weather_data:
   if hour_data['weather'][0]['id']<700:
       will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain🌧🌧.Bring umbrella!",
        from_='+13609001264',
        to='+92 307 5238297'
    )
    print(message.status)

