import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
import requests

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# *** ADDED: Prompt for city name and fetch coordinates via Geocoding API ***
city_name = input("Enter the city name: ")
geocode_url = "https://geocoding-api.open-meteo.com/v1/search"
geocode_params = {"name": city_name, "count": 1, "format": "json"}

resp = requests.get(geocode_url, params=geocode_params)
resp.raise_for_status()
geo_json = resp.json()
if not geo_json.get("results"):
    print("City not found.")
    exit()

location = geo_json["results"][0]
latitude = location["latitude"]
longitude = location["longitude"]
print(f"Coordinates for {city_name}: {latitude}, {longitude}")

# Original weather-fetching logic follows, now using dynamic coordinates
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation", "wind_speed_10m"],
    "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
    "timezone": "auto",
}
responses = openmeteo.weather_api(url, params=params)

response = responses[0]
print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation: {response.Elevation()} m asl")
print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

hourly_data = {
    "date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )
}
hourly_data["temperature_2m"] = hourly_temperature_2m

hourly_dataframe = pd.DataFrame(data=hourly_data)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print("\nHourly data\n", hourly_dataframe)