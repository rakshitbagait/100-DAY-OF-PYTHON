import requests
from datetime import datetime
API_ID = "7a12c3f4"

API_KEY ="06a43fb9195acbd0bac7097a9601c260"

exersice_endpoint ="https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("enter which exersice you did")
sheety_endpoint ="https://api.sheety.co/d13ca8adde33250ec2927351ccdde5c4/myWorkouts/workouts"
headers ={
    "Content-Type":"application/json",
    "x-app-id" :API_ID,
    "x-app-key": API_KEY
}
parameters = {
    "query": exercise_text,
    "gender": "male",        # or "female"
    "weight_kg": 70,
    "height_cm": 175,
    "age": 21
}

response = requests.post(url=exersice_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

    print(sheet_response.text)
    