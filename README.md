# Weather SDK

A simple SDK for interacting with the OpenWeatherMap API.

## Installation

You can install the package using pip:

pip install weather_sdk


# Usage
* First, initialize the SDK with your OpenWeatherMap API key:
from weather_sdk.sdk import WeatherSDK

sdk = WeatherSDK(api_key="YOUR_API_KEY_HERE")

* Get Weather by City Name
You can retrieve weather data for a city by its name:

data = sdk.get_weather_by_city_name("London")
print(data)


* Get Weather by Coordinates
You can retrieve weather data for a location using its latitude and longitude coordinates:

data = sdk.get_weather_by_coordinates(lat=51.51, lon=-0.13)
print(data)

* Replace "YOUR_API_KEY_HERE" with your actual OpenWeatherMap API key.


* Make sure to replace `"YOUR_API_KEY_HERE"` with your actual OpenWeatherMap API key in the usage examples.