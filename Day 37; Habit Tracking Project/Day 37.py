import requests
from datetime import datetime
from datetime import timedelta

USERNAME = "halasz"
TOKEN = "2JR#5nu#Bq#vnN"
GRAPH_ID = "graph1"
TODAY = datetime.now()
YESTERDAY = TODAY - timedelta(days=1)
YESTERDAY= YESTERDAY.strftime("%Y%m%d")
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
update_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_pixel_endpoint = f"{update_graph_endpoint}/{YESTERDAY}"
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{YESTERDAY}"
AMOUNT_LEARNED = input("How many hours have you learned today: ")

graph_header = {
    "X-USER-TOKEN": TOKEN,
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "Hours",
    "type": "float",
    "color": "shibafu",
}

graph_input = {
    "date": TODAY.strftime("%Y%m%d"),
    "quantity": AMOUNT_LEARNED,
}

config_yesterday = {
    "quantity": "2",
}

# user_response = requests.post(url=pixela_endpoint, json=user_params)
# print(user_response.text)

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_header)
# print(graph_response)

update_graph_response = requests.post(url=update_graph_endpoint, json=graph_input, headers=graph_header)
print(update_graph_response)

# config_yesterday_data = requests.put(url=update_pixel_endpoint, json=config_yesterday, headers=graph_header)
# print(config_yesterday_data)

# delete_pixel = requests.delete(url=delete_pixel_endpoint, headers=graph_header)
# print(delete_pixel.text)
