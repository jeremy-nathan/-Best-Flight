import geopy
from geopy.geocoders import Nominatim
from geopy import distance
import gmplot
import time
from djikstras import A
import random
start=time.time()

cities=['Kuala Lumpur','Shanghai','New York','Singapore','New Delhi','Manila','Washington DC','Tokyo','Paris']

cities_location={}
cities_coords={}
<<<<<<< HEAD
geolocator=Nominatim(user_agent="Algo Assignment",timeout=30)
=======
geolocator=Nominatim(user_agent="Algo Assignment", timeout = 70)
>>>>>>> 99f4bc6b6cdaaf7e5e8b1bda30a571b317e3abbd
cities_distance={}

for i in range(len(cities)):
    cities_location[cities[i]]=geolocator.geocode(cities[i])
    cities_coords[cities[i]]={}

for i in range(len(cities)):
    cities_coords[cities[i]]['latitude']=cities_location[cities[i]].latitude
    cities_coords[cities[i]]['longitude']=cities_location[cities[i]].longitude


def calcdistance(start):
<<<<<<< HEAD
     for i in range(len(cities)):
=======
    for i in range(0,len(cities)):
>>>>>>> 99f4bc6b6cdaaf7e5e8b1bda30a571b317e3abbd
        cities_distance[cities[start]][cities[i]]=int(distance.distance((cities_coords[cities[start]]['latitude'],cities_coords[cities[start]]['longitude']),(cities_coords[cities[i]]['latitude'],cities_coords[cities[i]]['longitude'])).kilometers)

counter = 0

for i in range(len(cities)):
    cities_distance[cities[i]]={}
    calcdistance(i)
    # while counter<9:
    #     if cities[counter] not in cities_distance[cities[i]]:
    #         calcdistance(i)
    #     counter+=1

dest  = input('Enter flight destination: ')
del cities_distance['Kuala Lumpur'][dest]

def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
    """ calculates a shortest path tree routed in src
    """
    # a few sanity checks
    if src not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if dest not in graph:
        raise TypeError('The target of the shortest path cannot be found')
    # ending condition
    if src == dest:
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        print('shortest path: '+str(path)+" cost="+str(distances[dest]))
    else :
        # if it is the initial  run, initializes the cost
        if not visited:
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,dest,visited,distances,predecessors)







# if __name__ == "__main__":
#     import sys
#     import unittest
    # sys.argv = ['', 'Test.testName']
    # unittest.main()
print()
print()

print()

print()


     # graph = {'s': {'a': 2, 'b': 1},
     #         'a': {'s': 3, 'b': 4, 'c':8},
     #         'b': {'s': 4, 'a': 2, 'd': 2},
     #         'c': {'a': 2, 'd': 7, 't': 4},
     #         'd': {'b': 1, 'c': 11, 't': 5},
     #         't': {'c': 3, 'd': 5}}
 #    dijkstra(graph,'s','t')
# print(cities_distance)


# for i in range(len(cities)-1):
dest=input("Enter your Destination: ")
del cities_distance['Kuala Lumpur'][dest]
dijkstra(cities_distance,'Kuala Lumpur',dest)
print()
# for i in range(len(cities)):
#     # for j in range(len(cities)):
#     if cities[4] not in cities_distance[cities[i]]:
#         print("shit")
#         counter+=1
#         if(counter ==9):
#             print("shit")
#         else:
#             continue
#     else:
#         break


end=time.time()

print("Running Time: ",(end-start))

# print(len(cities_distance['Kuala Lumpur']))
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
