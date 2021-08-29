import requests
import datetime
import smtplib
MY_LAT = 33.630013
MY_LNG = -286.890785


def is_iss_overhead():
    response_from_iss_website = requests.get(url="http://api.open-notify.org/iss-now.json")

    response_from_iss_website.raise_for_status()

    data = response_from_iss_website.json()['iss_position']

    longitude = data['longitude']
    latitude = data['latitude']
    if latitude >= MY_LAT - 5 and latitude <= MY_LAT + 5:
        if longitude >= MY_LNG - 5 and longitude <= MY_LAT + 5:
            return True


def is_night():
    date_and_time = datetime.datetime.now()
    time = date_and_time.hour
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response_from_sun_details_website = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_from_sun_details_website.raise_for_status()
    sun_data = response_from_sun_details_website.json()

    sunrise = int(sun_data['results']['sunrise'].split("T")[1].split(":")[0]) + 5
    sunset = int(sun_data['results']['sunset'].split("T")[1].split(":")[0]) + 5

    if time < sunrise or time > sunset:
        return True

if is_night() and is_iss_overhead() :
    my_email="bibliophilemuffie@gmail.com"
    my_password="0306872174182325"
    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=my_email,password=my_password)
        connect.sendmail(from_addr=my_email,
                             to_addrs=my_email,
                             msg="Subject:Look up👆\n\nthe international space station is above you")


