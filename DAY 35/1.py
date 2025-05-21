import requests

own_endpoint = "https://api.openweathermap.org/data/2.5/weather?lat=26.906966&lon=75.812302&appid=7b5660b31b654ba4c9dc9ce13a987e82"

api_key =  "7b5660b31b654ba4c9dc9ce13a987e82"
parameters = {
    "lat": 26.906966,
    "lon":75.812302,
    "appid": api_key,
    "cnt" : 4,
    }

response =requests.get(own_endpoint,params = parameters)
response.raise_for_status()
print(response.status_code)

weather_data = response.json
print(weather_data)

 

