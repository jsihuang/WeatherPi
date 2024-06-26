import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import st7735
import requests
import time

# import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
# from time import sleep # Import the sleep function from the time module

#GPIO.setwarnings(False) # Ignore warning for now
#GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
#GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)

# pin = digitalio.DigitalInOut(board.D14)
# print(pin.value)

# Define GPIO pins for LEDs
led_pin_1 = digitalio.DigitalInOut(board.D14)  # GPIO 14
led_pin_1.direction = digitalio.Direction.OUTPUT

led_pin_2 = digitalio.DigitalInOut(board.D15)  # GPIO 15
led_pin_2.direction = digitalio.Direction.OUTPUT

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

# icon folder directory
icon_dir = "./Icons"

# Blinking functions 
# def rain():
# 	GPIO.output(8, GPIO.HIGH) # Turn on
# 	sleep(0.2) # Sleep for 1 second
# 	GPIO.output(10, GPIO.HIGH) # Turn on
# 	GPIO.output(8, GPIO.LOW) # Turn on
# 	sleep(0.2) # Sleep for 1 second
# 	GPIO.output(10, GPIO.LOW) # Turn on

# def drizzle():
# 	GPIO.output(8, GPIO.HIGH) # Turn on
# 	sleep(2) # Sleep for 1 second
# 	GPIO.output(10, GPIO.HIGH) # Turn on
# 	GPIO.output(8, GPIO.LOW) # Turn off
# 	sleep(2) # Sleep for 1 second
# 	GPIO.output(10, GPIO.LOW) # Turn on


    

# Dictionary mapping weather icon codes to icon URLs
icon_urls = {
    "01d": "/01d.png",
    "01n": "/01n.png",
    "02d": "/02d.png",
    "02n": "/02n.png",
    "03d": "/03d.png",
    "03n": "03n.png",
    "04d": "/04d.png",
    "04n": "/04n.png",
    "09d": "/09d.png",
    "09n": "/09n.png",
    "10d": "/10d.png",
    "10n": "/10n.png",
    "11d": "/11d.png",
    "11n": "/11n.png",
    "13d": "/13d.png",
    "13n": "/13n.png",
    "50d": "/50d.png",
    "50n": "/50n.png"
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
        # get temperature
        temperature_kelvin = weather_data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        #get humidity
        humidity = weather_data['main']['humidity']
        # get wind speed
        # wind = weather_data['wind']['speed']
        # get weather description
        weather_description = weather_data['weather'][0]['description']
        icon_code = weather_data['weather'][0]['icon']
        icon_file = icon_urls.get(icon_code) #[0]
        

        def blink_leds_clear():
            for i in range(20):
                led_pin_1.value = True
                led_pin_2.value = True
                time.sleep(2)
                led_pin_1.value = False
                led_pin_2.value = False
                time.sleep(2)
        #         # Check if the weather icon has changed or condition is no longer met
        #         if '04' not in weather_data['weather'][0]['icon']:
        #             break  # Exit the loop if condition is no longer met

        def blink_leds_cloudy():
            #for review board 2024
            for i in range(20):
                led_pin_1.value = True
                time.sleep(0.2)
                led_pin_2.value = True
                led_pin_1.value = False
                time.sleep(0.2)
                led_pin_2.value = False
                time.sleep(0.2)
            
            # for i in range(20):
            #     led_pin_1.value = True
            #     led_pin_2.value = True
            #     time.sleep(0.5)
            #     led_pin_1.value = False
            #     led_pin_2.value = False
            #     time.sleep(0.5)
                # # Check if the weather icon has changed or condition is no longer met
                # if weather_data['weather'][0]['icon'] not in ['03d', '03n', '04d', '04n', '50d', '50n']:
                #     break  # Exit the loop if condition is no longer met

        def blink_leds_rain():
            for i in range(20):
                led_pin_1.value = True
                time.sleep(0.2)
                led_pin_2.value = True
                led_pin_1.value = False
                time.sleep(0.2)
                led_pin_2.value = False
                time.sleep(0.2)
        #         # Check if the weather icon has changed or condition is no longer met
        #         if '04' not in weather_data['weather'][0]['icon']:
        #             break  # Exit the loop if condition is no longer met

        # format weather icon
        icon_path = icon_dir + icon_file
        icon = Image.open(icon_path)
        icon = icon.resize((80, 80), Image.BICUBIC)
        
        # get UI icons
        icon_thermometer = Image.open("./Icons/thermometer_invert.png")
        icon_thermometer = icon_thermometer.resize((25, 25), Image.BICUBIC)
        icon_water = Image.open("./Icons/water-droplet_invert.png")
        icon_water = icon_water.resize((20, 20), Image.BICUBIC)
        
        # Create a blank image
        image = Image.new("RGB", (screen_width, screen_height))
        draw = ImageDraw.Draw(image)
        
        # Clear the screen
        draw.rectangle((0, 0, screen_width, screen_height), fill=(100, 100, 100))

        # Render weather information
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf", 18)
        
        draw.text((5, 10), f"{weather_description}",font=font, fill=(255, 255, 255))
        draw.text((50, 100), f"{temperature_celsius:.2f}°C", font=font, fill=(255, 255, 255))
        draw.text((50, 130), f"{humidity}%", font=font, fill=(255, 255, 255))
        
        # Paste the Icon
        # Image.Image.paste(image, icon, (50, 0))
        image.paste(icon, (24, 24), icon)
        image.paste(icon_thermometer, (15, 100), icon_thermometer)
        image.paste(icon_water, (15, 130), icon_water)

        # Display the image on the TFT screen
        display.image(image)

        #run blinking function
        # icon_urls.get(icon_code)[1]

        # Logs
        print(icon_path)
        print(f"Temperature: {temperature_celsius:.2f}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description}")

        #  # Check if weather icon indicates cloudy (cleary sky, few clouds)
        if weather_data['weather'][0]['icon'] in ['01d', '01n', '02d', '02n']:
            # Blinking function for cloudy
            blink_leds_clear()

         # Check if weather icon indicates cloudy (scattered, broken, mist)
        if weather_data['weather'][0]['icon'] in ['03d', '03n', '04d', '04n', '50d', '50n']:
            # Blinking function for cloudy
            blink_leds_cloudy()
        
        # Check if weather icon indicates rainy (shower, rain, thunderstorm, snow)
        elif weather_data['weather'][0]['icon'] in ['09d', '09n', '10d', '10n', '11d', '11n', '13d', '13n']:
            # Blinking function for rain
            blink_leds_rain()


    else:
        print("Weather data not found.")

# Main loop
while True:
    main()
    time.sleep(2)  # Update weather information every 2 seconds
