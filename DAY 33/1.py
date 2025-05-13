import requests
from datetime import datetime

MY_LAT = 26.850262
MY_LONG = 75.761726

# Get ISS location
iss_response = requests.get("http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_data = iss_response.json()
iss_longitude = float(iss_data["iss_position"]["longitude"])
iss_latitude = float(iss_data["iss_position"]["latitude"])

# Get sunrise/sunset data
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_response.raise_for_status()
sun_data = sun_response.json()

sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.utcnow().hour  # Use UTC time

# Check if ISS is nearby
is_iss_overhead = (
    abs(iss_latitude - MY_LAT) <= 5 and
    abs(iss_longitude - MY_LONG) <= 5
)

# Check if it's night
is_night = time_now < sunrise or time_now > sunset

if is_iss_overhead and is_night:
    print("Look up! The ISS is above you.")
else:
    print("No match.")
