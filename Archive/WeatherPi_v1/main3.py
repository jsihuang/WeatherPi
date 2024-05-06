import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import st7735
import requests
import time

# Define TFT screen dimensions
screen_width = 128
screen_height = 160

# Initialize TFT display
spi = board.SPI()
tft_cs = digitalio.DigitalInOut(board.CE0)
tft_dc = digitalio.DigitalInOut(board.D25)
tft_reset = digitalio.DigitalInOut(board.D24)

display = st7735.ST7735R(spi, cs=tft_cs, dc=tft_dc, rst=tft_reset, width=screen_width, height=screen_height)

# API URL and your API key
url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'
lat = 42.3601  # Latitude of Boston
lon = -71.0589  # Longitude of Boston
api_key = '10f152aed389023d1259b63224bc490a'
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
    "50n": "https://openweathermap.org/img/wn/50n.png"
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

        # Create a blank image
        image = Image.new("RGB", (screen_width, screen_height))
        draw = ImageDraw.Draw(image)

        # Clear the screen
        draw.rectangle((0, 0, screen_width, screen_height), fill=(0, 0, 0))

        # Render weather information
        font = ImageFont.load_default()
        draw.text((5, 5), f"Temperature: {temperature_celsius:.2f}°C", font=font, fill=(255, 255, 255))
        draw.text((5, 25), f"Humidity: {humidity}%", font=font, fill=(255, 255, 255))
        draw.text((5, 45), f"Weather: {weather_description}", font=font, fill=(255, 255, 255))

        # Display the image on the TFT screen
        display.image(image)

    else:
        print("Weather data not found.")

# Main loop
while True:
    main()
    time.sleep(60)  # Update weather information every 60 seconds
