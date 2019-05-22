
from geopy.geocoders import Nominatim
import geopy
from geopy import distance
import gmplot
import time

start=time.time()

cities=['Kuala Lumpur','Shanghai','New York','Singapore','New Delhi','Manila','Washington DC','Tokyo','Paris']

cities_location={}
cities_coords={}
geolocator=Nominatim(user_agent="Algo Assignment")
cities_distance={}

for i in range(len(cities)):
    cities_location[cities[i]]=geolocator.geocode(cities[i])
    cities_coords[cities[i]]={}

for i in range(len(cities)):
    cities_coords[cities[i]]['latitude']=cities_location[cities[i]].latitude
    cities_coords[cities[i]]['longitude']=cities_location[cities[i]].longitude


def calcdistance(start):
    for i in range(len(cities)):
        cities_distance[cities[start]][cities[i]]=int(distance.distance((cities_coords[cities[start]]['latitude'],cities_coords[cities[start]]['longitude']),(cities_coords[cities[i]]['latitude'],cities_coords[cities[i]]['longitude'])).kilometers)

for i in range(len(cities)):
    cities_distance[cities[i]]={}
    calcdistance(i)

print(cities_distance)
end=time.time()

print("Running Time: ",(end-start))
# cities_latitude=[None] * len(cities)
# cities_longitude=[None] * len(cities)
#
# origin='Kuala Lumpur'
# geolocator  = Nominatim(user_agent="Algo Assignment")
# KL_location=geolocator.geocode(origin)
# KL_latitude=KL_location.latitude
# KL_longitude=KL_location.longitude
#
# for i in range(len(cities)):
#     location=geolocator.geocode(cities[i])
#     cities_latitude[i]=location.latitude
#     cities_longitude[i]=location.longitude
#
# cities_latitude.append(KL_latitude)
# cities_longitude.append(KL_longitude)
#
# mymap=pygmaps.maps(KL_latitude,KL_longitude,15)
#
# for i in range(len(cities)):
#     mymap.addpoint(cities_latitude[i],cities_longitude[i],'#FF0000')
#
# city_coords=[()]*len(cities)
#
# for i in range(len(cities)):
#     city_coords[i]=(cities_latitude[i],cities_longitude[i])
#
# def add_path(start):
#     for i in range(len(cities)-1):
#         mymap.addpath(city_coords[0:(i+1)],"#FF0000")
#
# for i in range(len(cities)):
#     add_path(i)
#
# mymap.draw("gmap.html")
