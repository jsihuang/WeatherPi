import requests
from retrying import retry

@retry(stop_max_attempt_number=3, wait_fixed=1000)  # Retry 3 times with a 1-second delay
def get_weather():
    response = requests.get(weather_url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

# Main function to fetch and display weather information
def main():
    try:
        weather_data = get_weather()
        # Rest of your code...
    except Exception as e:
        print(f"Failed to fetch weather data: {e}")

