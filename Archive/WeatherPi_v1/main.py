import pygame
import requests

# API URL and your API key
url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'
lat = 42.3601  # Latitude of Boston
lon = -71.0589  # Longitude of Boston
api_key = '10f152aed389023d1259b63224bc490a'

# Format the URL with the latitude, longitude, and API key
weather_url = url.format(lat, lon, api_key)

# Dictionary mapping weather icon codes to icon URLs
icon_urls = {
    "01d": "https://openweathermap.org/img/wn/01d.png",
    "01n": "https://openweathermap.org/img/wn/01n.png",
    "02d": "https://openweathermap.org/img/wn/02d.png",
    "02n": "https://openweathermap.org/img/wn/02n.png",
    "03d": "https://openweathermap.org/img/wn/03d.png",
    "03n": "https://openweathermap.org/img/wn/03n.png",
    "04d": "https://openweathermap.org/img/wn/04d.png",
    "04n": "https://openweathermap.org/img/wn/04n.png",
    "09d": "https://openweathermap.org/img/wn/09d.png",
    "09n": "https://openweathermap.org/img/wn/09n.png",
    "10d": "https://openweathermap.org/img/wn/10d.png",
    "10n": "https://openweathermap.org/img/wn/10n.png",
    "11d": "https://openweathermap.org/img/wn/11d.png",
    "11n": "https://openweathermap.org/img/wn/11n.png",
    "13d": "https://openweathermap.org/img/wn/13d.png",
    "13n": "https://openweathermap.org/img/wn/13n.png",
    "50d": "https://openweathermap.org/img/wn/50d.png",
    "50n": "https://openweathermap.org/img/wn/50n.png",

    # Add more icon codes and URLs as needed
}

# Function to fetch weather data
def get_weather():
    response = requests.get(weather_url)
    data = response.json()
    return data

# Main function to fetch and display weather information
def main():
    weather_data = get_weather()
    if 'main' in weather_data:
        temperature_kelvin = weather_data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        humidity = weather_data['main']['humidity']
        weather_description = weather_data['weather'][0]['description']
        icon_code = weather_data['weather'][0]['icon']
        icon_url = icon_urls.get(icon_code)
        print(f"Temperature: {temperature_celsius:.2f}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description}")
        print(f"Icon URL: {icon_url}")
        print(temperature_celsius) #needs to take out
    else:
        print("Weather data not found.")

if __name__ == "__main__":
    main()