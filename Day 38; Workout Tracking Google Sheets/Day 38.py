import requests
from datetime import datetime

user_input = input("Tell me what exercises you did: ").lower()

BEARER_TOKEN = "{YOUR_BEARER_TOKEN}"
APPLICATION_ID = "{YOUR_APPLICATIO_ID}"
NUTRITIONIX_API_KEY = "{YOUR_API_KEY}"
USERNAME = "{YOU_USERNAME}"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/06c67c07c5c7a76e7db3005e5565d98a/myWorkoutsPython/workouts"

headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

nutritionix_params = {
    "query": user_input,
}

nutritionix_response = requests.post(url=EXERCISE_ENDPOINT, json=nutritionix_params, headers=headers)
data = nutritionix_response.json()

SHEETY_header = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}
for exercise in data["exercises"]:
    new_row = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": round(exercise["duration_min"]),
            "calories": round(exercise["nf_calories"]),
        }
    }
    exercise_response = requests.post(url=SHEETY_ENDPOINT, json=new_row, headers=SHEETY_header)
