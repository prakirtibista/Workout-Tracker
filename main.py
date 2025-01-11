import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
# API credentials and endpoints
ID = os.environ.get('APP_ID')
KEY = os.environ.get('APP_KEY')
ENDPOINT = os.environ.get('NUTRITION_ENDPOINT')
URL = os.environ.get('SHEETY_URL')
TOKEN = os.environ.get('SHEETY_TOKEN')
WEIGHT=os.environ.get('WEIGHT')
AGE=os.environ.get('AGE')
HEIGHT=os.environ.get('HEIGHT')


headers = {
    "x-app-id": ID,
    "x-app-key": KEY
}


exercise_query = input("What exercise did you do? ")

params = {
    "query": exercise_query,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(ENDPOINT, json=params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    'Authorization': f"Basic {TOKEN}"
}


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

    sheet_response = requests.post(URL, json=sheet_inputs, headers=bearer_headers)


