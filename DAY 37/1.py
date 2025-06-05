import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "rakshitbagait"
TOKEN = "ajlkdslfjljio3424"
GRAPH = "my_graph100"# Defined TOKEN

user_params  = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create User (Uncomment to run only once)
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color":"sora",  # Fixed typo here
}

headers = {
    "X-USER-TOKEN": TOKEN
}
today = datetime(year=2025,month=6,day=5)
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

pixela_endpoint_creation = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

pixel_data = {
    "date": "20200724",
    "quantity":"9.52",

}
requests.post(url=pixela_endpoint_creation,json=pixel_data,headers=headers)
print(response.text)