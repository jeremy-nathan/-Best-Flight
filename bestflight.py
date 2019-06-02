from geopy.geocoders import Nominatim
import geopy
from geopy import distance
import gmplot
import time
import gmplot


start=time.time()


cities=['Kuala Lumpur','Shanghai','New York','Singapore','New Delhi','Manila','Washington DC','Tokyo','Paris']
cities_latitude=[None] * len(cities)
cities_longitude=[None] * len(cities)

origin='Kuala Lumpur'
geolocator  = Nominatim(user_agent="Algo Assignment")
KL_location=geolocator.geocode(origin,timeout = 150)
KL_latitude=KL_location.latitude
KL_longitude=KL_location.longitude


geolocator  = Nominatim(user_agent="Algo Assignment")
for i in range(len(cities)):
    location=geolocator.geocode(cities[i],timeout=120)
    cities_latitude[i]=location.latitude
    cities_longitude[i]=location.longitude


gmap3 = gmplot.GoogleMapPlotter(KL_latitude,
                                KL_longitude, 13)

gmap3.scatter( cities_latitude, cities_longitude, '#FF0000',
                              size = 100, marker = True )

gmap3.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
gmap3.marker(cities_latitude[0],cities_longitude[0],'cornflowerblue')

for i in range(len(cities)):
    gmap3.plot(cities_latitude[0:(i+1)], cities_longitude[0:(i+1)],
           'red', edge_width = 2.5)
gmap3.plot(cities_latitude[0:2],cities_longitude[0:2], 'red',edge_width = 2.5)

for j in range(len(cities_latitude)):
    for i in range(len(cities_latitude)-1):
        gmap3.plot((cities_latitude[j],cities_latitude[i+1]),(cities_longitude[j],cities_longitude[i+1]), 'red',edge_width = 2.5)


gmap3.apikey="AIzaSyDmpwQtMwmoWGHX2UBqnAldc8CFDus77RQ"

for j in range(len(cities)):
     for i in range(len(cities)):
         gmap3.plot(cities_latitude[j:i],cities_longitude[j:i], 'red',edge_width = 2.5)


gmap3.draw("gmap.html")
