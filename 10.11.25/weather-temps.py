import requests
import datetime

API_KEY = "2ddc2778a6aca42b28612d3a5f5acbf0"
BASE_CURRENT_URL = "http://api.weatherstack.com/current"
BASE_FORECAST_URL = "http://api.weatherstack.com/forecast"

def get_current_weather(location):
    params = {
        "access_key": API_KEY,
        "query": location
    }
    resp = requests.get(BASE_CURRENT_URL, params=params)
    data = resp.json()
    if not data.get("success", True):
        raise Exception(data["error"]["info"])
    return data

def get_week_forecast(location):
    params = {
        "access_key": API_KEY,
        "query": location,
        "forecast_days": 7,
        "hourly": 0
    }
    resp = requests.get(BASE_FORECAST_URL, params=params)
    data = resp.json()
    if not data.get("success", True):
        raise Exception(data["error"]["info"])
    return data["forecast"]

def print_weather(location):
    # Current weather
    curr = get_current_weather(location)
    loc = curr["location"]["name"]
    curr_info = curr["current"]
    print(f"📍 Current weather in {loc}:")
    print(f"  🌡 Temperature: {curr_info['temperature']}°C")
    print(f"  {', '.join(curr_info['weather_descriptions'])}")
    print(f"  Feels like: {curr_info['feelslike']}°C")
    print(f"  💧 Humidity: {curr_info['humidity']}%")
    print(f"  🌬 Wind: {curr_info['wind_speed']} km/h {curr_info['wind_dir']}\n")

if __name__ == "__main__":
    print_weather("London")