import requests
import dotenv


def get_weather_from_openweather(api_key, city_name="London"): 
    base_url = "http://api.openweathermap.org/data/2.5/weather"
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
    API_KEY = "8eb3ab622fcf31d0f9a779736017be18"
    weather = get_weather_from_openweather(API_KEY)
    
    if weather:
        print(f"Weather in {weather['name']}:")
        print(f"Temp: {weather['main']['temp']}")
        print(f"Info: {weather['weather'][0]['description']}")
