import requests
import datetime
PIXELA_API_ADDRESS="https://pixe.la/v1/users"
USERNAME="dotdot"
TOKEN="jkzfvhoiau9cxjccxvd"
pixela_params={
    "token":"jkzfvhoiau9cxjccxvd",
    "username":"dotdot",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response_from_pixela=requests.post(url=PIXELA_API_ADDRESS,json=pixela_params)
# print(response_from_pixela.text)
GRAPH_ID="healthgraph1"
PIXELA_API_GRAPH_ADDRESS=f"{PIXELA_API_ADDRESS}/{USERNAME}/graphs"
graph_param={
    "id":GRAPH_ID,
    "name":"Walking Graph",
    "unit":"KM",
    "type":"float",
    "color":"shibafu"
}
headers={
    "X-USER-TOKEN":TOKEN
}
# response_from_graph_pixela=requests.post(url=PIXELA_API_GRAPH_ADDRESS,json=graph_param,headers=headers)
# print(response_from_graph_pixela.text)

PIXELA_API_PIXEL_ADDRESS=f"{PIXELA_API_ADDRESS}/{USERNAME}/graphs/{GRAPH_ID}"
today=datetime.date.today()
today=str(today-datetime.timedelta(days=1))
today=today.replace("-","")
pixela_params={
    'date':today,
    'quantity':'3.9',
}
# response_from_pixel_pixela=requests.post(url=PIXELA_API_PIXEL_ADDRESS,json=pixela_params,headers=headers)
# print(response_from_pixel_pixela.text)
PIXELA_API_PIXEL_UPDATE_ADDRESS=f"{PIXELA_API_PIXEL_ADDRESS}/{today}"
print(PIXELA_API_PIXEL_UPDATE_ADDRESS)

pixela_update_params={
    'quantity':'1.5',
}

response_from_pixel_update_pixela=requests.put(url=PIXELA_API_PIXEL_UPDATE_ADDRESS,json=pixela_update_params,headers=headers)
print(response_from_pixel_update_pixela.text)
response_from_pixel_update_pixela.raise_for_status()

response_from_pixel_update_pixela=requests.delete(url=PIXELA_API_PIXEL_UPDATE_ADDRESS,json=pixela_update_params,headers=headers)