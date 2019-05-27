from geopy.geocoders import Nominatim
import geopy
from geopy import distance
import gmplot


cities=['Kuala Lumpur','Shanghai','New York','Singapore','New Delhi','Manila','Washington DC','Tokyo','Paris']
cities_latitude=[None] * len(cities)
cities_longitude=[None] * len(cities)

origin='Kuala Lumpur'
geolocator  = Nominatim(user_agent="Algo Assignment")
KL_location=geolocator.geocode(origin,timeout = 200)
KL_latitude=KL_location.latitude
KL_longitude=KL_location.longitude

geolocator  = Nominatim(user_agent="Algo Assignment")
for i in range(len(cities)):
    location=geolocator.geocode(cities[i],timeout=150)
    cities_latitude[i]=location.latitude
    cities_longitude[i]=location.longitude



gmap4 = gmplot.GoogleMapPlotter(KL_latitude,
                                KL_longitude, 13)

gmap4.scatter( cities_latitude, cities_longitude, '#FF0000',
                              size = 100, marker = True )

gmap4.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
gmap4.marker(cities_latitude[0],cities_longitude[0],'cornflowerblue')

gmap4.apikey="AIzaSyDmpwQtMwmoWGHX2UBqnAldc8CFDus77RQ"


gmap4.draw("gmap4.html")
