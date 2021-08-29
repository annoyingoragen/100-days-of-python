import requests

parameters={
    "amount":10,
    'type':'boolean'
}
response_from_quiz_web=requests.get(url="https://opentdb.com/api.php",params=parameters)

data_from_web=response_from_quiz_web.json()
question_data=data_from_web['results']


