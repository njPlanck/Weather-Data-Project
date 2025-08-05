import requests

api_key = '95defe9036e30da886bdba5da3b70d12'
api_url = f'http://api.weatherstack.com/current?access_key={api_key}&query=New York'


def fetch_data():
    print("Fetching weather data drom weather API...")
    try:
        # --- ADD THIS DEBUG PRINT ---
        print(f"DEBUG: Requesting URL: {api_url}")
        # --- END DEBUG PRINT ---
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response recieved successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print("An error occured: {e}")
        raise

#fetch_data()


'''
def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-07-25 13:41', 'localtime_epoch': 1753450860, 'utc_offset': '-4.0'}, 'current': {'observation_time': '05:41 PM', 'temperature': 35, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '05:47 AM', 'sunset': '08:18 PM', 'moonrise': '06:24 AM', 'moonset': '09:12 PM', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 0}, 'air_quality': {'co': '405.15', 'no2': '18.315', 'o3': '152', 'so2': '12.21', 'pm2_5': '26.64', 'pm10': '27.565', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 12, 'wind_degree': 250, 'wind_dir': 'WSW', 'pressure': 1013, 'precip': 0, 'humidity': 45, 'cloudcover': 50, 'feelslike': 42, 'uv_index': 9, 'visibility': 16, 'is_day': 'yes'}}
'''