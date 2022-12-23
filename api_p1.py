import urllib.request as url
import json
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="App_1")

location = input("Enter city/state/country : ")
coords = geolocator.geocode(location)
lat = coords.latitude
lon = coords.longitude
path = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=83e01e3dce5d28839bb5a177cb51af12"

response = url.urlopen(path)
data = json.load(response)
k = data['main']['temp']
c = k - 273.15
print(f"Temp in {location} is {c:.2f}")
