import requests
import smtplib

my_email ="rbagait2018@gmail.com"
password ="ypan zgfy iwhx hfuy"
connection =smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()

own_endpoint = "https://api.openweathermap.org/data/2.5/forecast?lat=26.906966&lon=75.812302&appid=7b5660b31b654ba4c9dc9ce13a987e82"

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

weather_data = response.json()
# print(weather_data["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code)<700:
        will_rain = True
if will_rain:
    print("bring an umbrella")
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="rakshitbagaitpcm@gmail.com",msg="Subject:Bring Umbrella\n\nIt will  rain today so carry an umberella")
    connection.close()
else : print("normal")

