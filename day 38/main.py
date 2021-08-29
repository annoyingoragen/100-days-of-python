APP_ID="f1c327f3"
API_KEY="14959c9290c71c8ff9febff8700063c7"

import requests
import datetime
import os
NUTRITION_API="https://trackapi.nutritionix.com/v2/natural/exercise"
exercises=input('Tell me which exercise you did: ')
exercise_param={
    'query':exercises,
    "gender": "female",
    "weight_kg": 75.5,
    "height_cm": 165,
    "age": 24
}
headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}

response_from_nutrition_website=requests.post(NUTRITION_API,json=exercise_param,headers=headers)
response_from_nutrition_website.raise_for_status()
exercises=response_from_nutrition_website.json()['exercises']


SHEETY_POST_API="https://api.sheety.co/63d30f193ee6e5d12376d1c02140e96a/dotsWorkouts/workouts"
today=datetime.datetime.today()
today=today.strftime("%x")
time=datetime.datetime.time(datetime.datetime.now())
time=str(time)
time=time.split(".")[0]


for exercise in exercises:

    sheety_params={
         'workout':{
             'date':today,
             'time':time,
             'exercise':exercise['name'],
             'duration':exercise['duration_min'],
             'calories':exercise['nf_calories']

           }

    }
    print(os.environ.get('SHEETY_TOKEN'))
    headers={
        "Authorization": f"Bearer {os.environ.get('SHEETY_TOKEN')}"
    }
    response_from_sheety_website=requests.post(url=SHEETY_POST_API,json=sheety_params,headers=headers)
    response_from_sheety_website.raise_for_status()
    print(response_from_sheety_website.json())
