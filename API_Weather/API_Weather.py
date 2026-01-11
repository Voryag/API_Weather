from matplotlib.pylab import f
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

    def get_weather(self, city: str) -> dict :
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
            return data

        except requests.exceptions.Timeout:
            self.logger.error(f"Таймайут при запросе для {city}")
            print("Превышено время ожидания ответа от сервера")
        except request.exceptions.ConnectionError:
            self.logger.error(f"Ошибка подключения для {city}")
            print("Проблема с подключением к интернету")
        except request.exceptions.HTTPError as http_err:
            error_data = response.json() if response else {}
            error_msg = error_data.get("message", "Неизвестная ошибка API")

            if response.status_code == 404:
                self.logger.warning(f"Город не найден")
                print(f"Город {city} не найден")
            else:
                self.logger.error(f"Ошибка API (код {response.status_code}) : {error_msg}")   
                print(f"Ошибка API: {error_msg}")
        except Exception as e:
            self.logger.critical(f"Непредвиденная ошибка: {e}", exc_info=True)
            print(f"Ошибка API: {error_msg}")

        return None

    def display_weather(self, weather_data: dict) -> None:
        if not weather_data:
            print("Нет данных для отображения")
            return

        city = weather_data["name"]
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        feels_like = weather_data["main"].get("feels_like", temp)

        print(f"\n{'='*40}")
        print(f"🌤  ПОГОДА В {city.upper()}")
        print(f"{'='*40}")
        print(f"📊 Температура: {temp}°C (ощущается как {feels_like}°C)")
        print(f"💧 Влажность: {humidity}%")
        print(f"📝 Описание: {description.capitalize()}")
        print(f"{'='*40}\n")



    def get_weather_from_openweather(api_key, city_name="London"): 
        params = {
            'q': city_name,
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
