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
        self.logger.info("WearherService is initialized")

    def _setup_logging(self):
        self.logger = logging.getLogger(WeatherService)

        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
                )

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def get_weather(self, city: str) -> dict | None:
        self.logger.info(f"Запрос погоды для города: {city}")

        params = {
            "q": city_name,
            "appid": api_key,
            "units": "metric",
            "lang": "ru",
            }

        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            self.logger.info(f"Получена информация для города: {city}")

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
