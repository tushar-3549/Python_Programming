from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
@app.get('/')
def home():
    return {"message": "welcome to api integration"}

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

@app.get("/weather/")
def get_weather(city: str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    else:
        return {"error": "city not found"}