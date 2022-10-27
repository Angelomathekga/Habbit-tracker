import requests
from datetime import datetime

pixels_endpoint = "https://pixe.la/v1/users"
TOKEN = "Angelo663#@"
USERNAME = "angelzilla"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixels_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixels_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)
today = datetime.now()
values_endpoint = f"{pixels_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
values_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many km did you run today?")
}
response = requests.post(url=values_endpoint, json=values_data, headers=header)
print(response.text)

update_enpoint = f"{pixels_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_value_data = {
    "quantity": "4.6"
}

# response = requests.put(url=update_enpoint, json=new_value_data, headers=header)
# print(response.text)