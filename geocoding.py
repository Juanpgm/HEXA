from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="addressGeocoding")
location = geolocator.geocode("Cl. 42 #7b-52 a 7b-72, Ibagué, Tolima")

print(location.address)

print((location.latitude, location.longitude))