import pygmaps
from geopy.geocoders import Nominatim
import geopy
from geopy import distance
import gmplot

cities=['Kuala Lumpur','Shanghai','New York','Singapore','New Delhi','Manila','Washington DC','Tokyo','Paris']
cities_latitude=[None] * len(cities)
cities_longitude=[None] * len(cities)

origin='Kuala Lumpur'
geolocator  = Nominatim(user_agent="Algo Assignment")
KL_location=geolocator.geocode(origin)
KL_latitude=KL_location.latitude
KL_longitude=KL_location.longitude

for i in range(len(cities)):
    location=geolocator.geocode(cities[i])
    cities_latitude[i]=location.latitude
    cities_longitude[i]=location.longitude

cities_latitude.append(KL_latitude)
cities_longitude.append(KL_longitude)

mymap=pygmaps.maps(KL_latitude,KL_longitude,15)

for i in range(len(cities)):
    mymap.addpoint(cities_latitude[i],cities_longitude[i],'#FF0000')

city_coords=[()]*len(cities)

for i in range(len(cities)):
    city_coords[i]=(cities_latitude[i],cities_longitude[i])

def add_path(start):
    for i in range(len(cities)-1):
        mymap.addpath(city_coords[0:(i+1)],"#FF0000")

for i in range(len(cities)):
    add_path(i)

mymap.draw("gmap.html")
