from geopy.geocoders import Nominatim
import geopy
###import gmplot

cities=['Shanghai','New York','Singapore','New Delhi','Manila','Washington DC','Tokyo','Paris']
cities_latitude=[None] * len(cities)
cities_longitude=[None] * len(cities)

origin='Kuala Lumpur'
geolocator  = Nominatim(user_agent="Algo Assignment")
KL_location=geolocator.geocode(origin)
KL_latitude=KL_location.latitude
KL_longitude=KL_location.longitude
# from geopy.geocoders import Nominatim
print((KL_latitude,KL_longitude))


for i in range(len(cities)):
    location=geolocator.geocode(cities[i])
    cities_latitude[i]=location.latitude
    cities_longitude[i]=location.longitude
cities_latitude.append(KL_latitude)
cities_longitude.append(KL_longitude)

print(cities_latitude)
print(cities_longitude)
# print(location.raw)

import gmplot

gmap3 = gmplot.GoogleMapPlotter(KL_latitude,
                                KL_longitude, 13)

gmap3.scatter( cities_latitude, cities_longitude, '#FF0000',
                              size = 40, marker = False )

gmap3.plot(cities_latitude, cities_longitude,
           'red', edge_width = 2.5)

gmap3.draw("gmap3.html")
