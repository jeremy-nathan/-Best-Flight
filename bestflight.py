from geopy.geocoders import Nominatim
import geopy
from geopy import distance
import gmplot
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import networkx as nx
import time

start=time.time()


cities=['Kuala Lumpur','Shanghai','New York','Singapore','New Delhi','Manila','Washington DC','Tokyo','Paris']
cities_latitude=[None] * len(cities)
cities_longitude=[None] * len(cities)

origin='Kuala Lumpur'
geolocator  = Nominatim(user_agent="Algo Assignment")
KL_location=geolocator.geocode(origin)
KL_latitude=KL_location.latitude
KL_longitude=KL_location.longitude
# from geopy.geocoders import Nominatim
print((KL_latitude,KL_longitude))

origin2 = 'Shanghai'
Shanghai_location =geolocator.geocode(origin2)
Shanghai_latitude =Shanghai_location.latitude
Shanghai_longitude = Shanghai_location.longitude




for i in range(len(cities)):
    location=geolocator.geocode(cities[i])
    cities_latitude[i]=location.latitude
    cities_longitude[i]=location.longitude

cities_latitude.append(KL_latitude)
cities_longitude.append(KL_longitude)

print(cities_latitude)
print(cities_longitude)
# print(location.raw)

print()
cities_distance=[None] * len(cities)

for i in range(len(cities)):
    print("Distance between "+cities[0]+" and "+cities[i])
    cities_distance[i]=int(distance.distance((cities_latitude[0],cities_longitude[0]),(cities_latitude[i],cities_longitude[i])).kilometers)



cities_distance_Shanghai ={}
for i in range(len(cities)):
    cities_distance_Shanghai[cities[i]] = int(distance.distance((Shanghai_latitude,Shanghai_longitude),(cities_latitude[i],cities_longitude[i])).kilometers)

print("Shanghai")
print(cities_distance_Shanghai)

origin3 = 'New York'
NewYork_location =geolocator.geocode(origin3)
NewYork_latitude =NewYork_location.latitude
NewYork_longitude = NewYork_location.longitude



cities_distance_NewYork = {}
for i in range(len(cities)):
    cities_distance_NewYork[cities[i]] = int(distance.distance((NewYork_latitude,NewYork_longitude),(cities_latitude[i], cities_longitude[i])).kilometers)
print('New York')
print(cities_distance_NewYork)


origin4 = 'Singapore'
Singapore_location =geolocator.geocode(origin4)
Singapore_latitude =Singapore_location.latitude
Singapore_longitude = Singapore_location.longitude



cities_distance_Singapore = {}
for i in range(len(cities)):
    cities_distance_Singapore[cities[i]] = int(distance.distance((Singapore_latitude,Singapore_longitude),(cities_latitude[i], cities_longitude[i])).kilometers)
print('Singapore')
print(cities_distance_Singapore)

origin5 = 'New Delhi'
New_Delhi_location = geolocator.geocode(origin5)
New_Delhi_latitude =New_Delhi_location.latitude
New_Delhi_longitude = New_Delhi_location.longitude



cities_distance_New_Delhi = {}

for i in range(len(cities)):
     cities_distance_New_Delhi[cities[i]] = int(distance.distance((New_Delhi_latitude,New_Delhi_longitude),(cities_latitude[i], cities_longitude[i])).kilometers)
print('New Delhi')
print(cities_distance_New_Delhi)


origin6 = 'Manila'
Manila_location = geolocator.geocode(origin6)
Manila_latitude = Manila_location.latitude
Manila_longitude = Manila_location.longitude

cities_distance_Manila = {}

for i in range(len(cities)):
     cities_distance_Manila[cities[i]] = int(distance.distance((Manila_latitude,Manila_longitude),(cities_latitude[i], cities_longitude[i])).kilometers)
print('Manila')
print(cities_distance_Manila)

origin7 = 'Washington DC'
Washington_DC_location = geolocator.geocode(origin7)
Washington_DC_latitude = Washington_DC_location.latitude
Washington_DC_longitude = Washington_DC_location.longitude


cities_distance_Washington_DC = {}

for i in range(len(cities)):
     cities_distance_Washington_DC[cities[i]] = int(distance.distance((Washington_DC_latitude,Washington_DC_longitude),(cities_latitude[i], cities_longitude[i])).kilometers)
print('Washington DC')
print(cities_distance_Washington_DC)

origin8 = 'Tokyo'
Tokyo_location = geolocator.geocode(origin8)
Tokyo_latitude = Tokyo_location.latitude
Tokyo_longitude = Tokyo_location.longitude


cities_distance_Tokyo = {}

for i in range(len(cities)):
     cities_distance_Tokyo[cities[i]] = int(distance.distance((Tokyo_latitude,Tokyo_longitude),(cities_latitude[i], cities_longitude[i])).kilometers)
print('Tokyo')
print(cities_distance_Tokyo)


origin9 = 'Paris'
Paris_location = geolocator.geocode(origin9)
Paris_latitude = Paris_location.latitude
Paris_longitude = Paris_location.longitude


cities_distance_Paris = {}

for i in range(len(cities)):
     cities_distance_Paris[cities[i]] = int(distance.distance((Paris_latitude,Paris_longitude),(cities_latitude[i], cities_longitude[i])).kilometers)
print('Paris')
print(cities_distance_Paris)



import gmplot
import numpy as np
import pandas as pd

gmap3 = gmplot.GoogleMapPlotter(KL_latitude,
                                KL_longitude, 13)

gmap3.scatter( cities_latitude, cities_longitude, '#FF0000',
                              size = 40, marker = False )
# for i in range(len(cities)):
#     gmap3.plot(cities_latitude[0:(i+1)], cities_longitude[0:(i+1)],
#            'red', edge_width = 2.5)
gmap3.plot(cities_latitude[0:2],cities_longitude[0:2], 'red',edge_width = 2.5)

for j in range(len(cities_latitude)):
    for i in range(len(cities_latitude)-1):
        gmap3.plot((cities_latitude[j],cities_latitude[i+1]),(cities_longitude[j],cities_longitude[i+1]), 'red',edge_width = 2.5)
#gmap3.plot(cities_latitude[0:4],cities_longitude[0:4], 'red',edge_width = 2.5)

# def add_line(start):
#     for i in range(len(cities)):


gmap3.apikey="AIzaSyDmpwQtMwmoWGHX2UBqnAldc8CFDus77RQ"


gmap3.draw("gmap3.html")

G = nx.Graph()

def add_node(startnode):
    for i in range(len(cities)-1):
        G.add_edge(cities[startnode],cities[i+1],weight=cities_distance[i+1])


for i in range(len(cities)):
    add_node(i)

pos  = nx.spring_layout(G)

nx.draw_networkx_nodes(G,pos,node_size = 700)

nx.draw_networkx_edges(G,pos,edgelist=None, width = 6)

nx.draw_networkx_labels(G,pos,font_size = 10, font_family = 'sans-serif')

plt.axis('off')
plt.show()

end=time.time()

print("Running Time: "+str(end-start))
