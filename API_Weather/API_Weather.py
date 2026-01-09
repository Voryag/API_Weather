import requests
import dotenv
import logging
from config import API_KEY


class WeatherService:
    """Class for take information with API"""

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
                

    def __init__(self, api_key: str):
        self.api_key = api_key
        self._setup_logging()
        self.logger.info("WearherService is initialiez")

    def get_weather_from_openweather(api_key, city_name="London"): 
        params = {
            "q": city_name,
            "appid": api_key,
            "units": "metric",
            "lang": "ru",
            }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None


if __name__ == "__main__":
    weather = get_weather_from_openweather(API_KEY)
    
    if weather:
        print(f"Weather in {weather['name']}:")
        print(f"Temp: {weather['main']['temp']}")
        print(f"Info: {weather['weather'][0]['description']}")
