import geopy
from geopy.geocoders import Nominatim
from geopy import distance
import gmplot
import time
import random
start=time.time()
import webbrowser
from itertools import combinations

origin='Kuala Lumpur'
geolocator  = Nominatim(user_agent="Algo Assignment")
KL_location=geolocator.geocode(origin,timeout=100)
KL_latitude=KL_location.latitude
KL_longitude=KL_location.longitude
cities=['Kuala Lumpur','Shanghai','New York','Singapore','New Delhi','Washington DC','Tokyo','Paris','Manila']
cities_latitude=[None] * len(cities)
cities_longitude=[None] * len(cities)
for i in range(len(cities)):
    location=geolocator.geocode(cities[i],timeout =150)
    cities_latitude[i]=location.latitude
    cities_longitude[i]=location.longitude

gmap3 = gmplot.GoogleMapPlotter(KL_latitude,KL_longitude,13)
gmap3.scatter(cities_latitude,cities_longitude,'#FF0000',20, True)

cities_latitude.append(KL_latitude)
cities_longitude.append(KL_longitude)
cities_location={}
cities_coords={}
geolocator=Nominatim(user_agent="Algo Assignment",timeout=30)
cities_distance={}
comb_distance = list(combinations(['Kuala Lumpur','Shanghai','New York','Singapore','New Delhi','Manila','Washington DC','Tokyo','Paris'],2))

for i in range(len(cities)):
    cities_location[cities[i]]=geolocator.geocode(cities[i])
    cities_coords[cities[i]]={}

for i in range(len(cities)):
    cities_coords[cities[i]]['latitude']=cities_location[cities[i]].latitude
    cities_coords[cities[i]]['longitude']=cities_location[cities[i]].longitude


def calcdistance(start):
    for i in range(0,len(cities)):
        cities_distance[cities[start]][cities[i]]=int(distance.distance((cities_coords[cities[start]]['latitude'],cities_coords[cities[start]]['longitude']),(cities_coords[cities[i]]['latitude'],cities_coords[cities[i]]['longitude'])).kilometers)



for i in range(len(cities)):
    cities_distance[cities[i]]={}
    calcdistance(i)


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
        path_location = [None] *4
        path_latitude = [None] *4
        path_longitude = [None] *4
        pred=dest


        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        for i in range(len(path)):
            path_location[i] = geolocator.geocode(path[i])
            path_latitude[i] = path_location[i].latitude
            path_longitude[i] = path_location[i].longitude
        print(path_latitude)


        for i in range (len(cities_coords)):
              gmap3.plot(path_latitude,path_longitude,'red', edge_width = 3.0)

        print('shortest path: '+str(path))
        print(" Total Distance : "+str(distances[dest]) + " kilometres")
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

KL_Manila_Route = {'Kuala Lumpur':{'Singapore':cities_distance['Kuala Lumpur']['Singapore'],'New Delhi':cities_distance['Kuala Lumpur']['New Delhi'],'Paris':cities_distance['Kuala Lumpur']['Paris'], 'Washington DC':cities_distance['Kuala Lumpur']['Washington DC']},
                    'Singapore':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Singapore'],'Shanghai':cities_distance['Singapore']['Shanghai'],'Tokyo':cities_distance['Singapore']['Tokyo']},
                    'New Delhi':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['New Delhi'],'New York':cities_distance['New Delhi']['New York']},
                    'Paris':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Paris'],'Shanghai':cities_distance['Shanghai']['Paris']},
                    'Shanghai':{'Singapore':cities_distance['Singapore']['Shanghai'],'Manila':cities_distance['Manila']['Shanghai'],'Paris':cities_distance['Shanghai']['Paris'],'Washington DC':cities_distance['Shanghai']['Washington DC']},
                    'Tokyo':{'Singapore':cities_distance['Singapore']['Tokyo'],'Manila':cities_distance['Manila']['Tokyo']},
                    'Washington DC':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Washington DC'],'Shanghai':cities_distance['Shanghai']['Washington DC'],"New York":cities_distance["New York"]["Washington DC"]},
                    'New York':{'New Delhi':cities_distance['New York']['New Delhi'], 'Manila':cities_distance['New York']['Manila']},
                    'Manila':{'Tokyo':cities_distance['Tokyo']['Manila'],'Shanghai':cities_distance['Shanghai']['Manila'],'New York':cities_distance["New York"]['Manila'],"Singapore":cities_distance["Singapore"]["Manila"]}}

KL_Tokyo_Route = {'Kuala Lumpur':{'Washington DC':cities_distance['Kuala Lumpur']['Washington DC'],'Singapore':cities_distance['Kuala Lumpur']['Singapore'],'New Delhi':cities_distance['Kuala Lumpur']['New Delhi'], 'Paris':cities_distance['Paris']['Kuala Lumpur']},
                  'Singapore':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Singapore'],'Manila':cities_distance['Singapore']['Manila'],'Shanghai':cities_distance['Singapore']['Shanghai']},
                'New Delhi':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['New Delhi'], 'Shanghai':cities_distance['Shanghai']['New Delhi']},
                'Paris':{'Kuala Lumpur':cities_distance['Paris']['Kuala Lumpur'],'Manila':cities_distance['Paris']['Manila']},
                'Washington DC':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Washington DC'],'Manila':cities_distance['Washington DC']['Manila']},
                'Manila':{'Paris':cities_distance['Paris']['Manila'],'Washington DC':cities_distance['Washington DC']['Manila'], 'Singapore':cities_distance['Manila']['Singapore'],'Tokyo':cities_distance['Manila']['Tokyo']},
                'Shanghai':{'New Delhi':cities_distance['Shanghai']['New Delhi'],'Singapore':cities_distance['Singapore']['Shanghai'],'Tokyo':cities_distance['Tokyo']['Shanghai']},
                'Tokyo':{'Manila':cities_distance['Manila']['Tokyo'],'Shanghai':cities_distance['Tokyo']['Shanghai']}}


KL_NewDelhi_Route = {'Kuala Lumpur':{'Washington DC':cities_distance['Kuala Lumpur']['Washington DC'],'Singapore':cities_distance['Kuala Lumpur']['Singapore'],'Tokyo':cities_distance['Kuala Lumpur']['Tokyo'], 'Paris':cities_distance['Paris']['Kuala Lumpur']},
                'Singapore':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Singapore'],'Manila':cities_distance['Singapore']['Manila'],'Shanghai':cities_distance['Singapore']['Shanghai']},
                'Tokyo':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Tokyo'], 'Shanghai':cities_distance['Shanghai']['Tokyo']},
                'Paris':{'Kuala Lumpur':cities_distance['Paris']['Kuala Lumpur'],'Manila':cities_distance['Paris']['Manila']},
                'Washington DC':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Washington DC'],'Manila':cities_distance['Washington DC']['Manila']},
                'Manila':{'Paris':cities_distance['Paris']['Manila'],'Washington DC':cities_distance['Washington DC']['Manila'], 'Singapore':cities_distance['Manila']['Singapore'],'Tokyo':cities_distance['Manila']['Tokyo']},
                'Shanghai':{'New Delhi':cities_distance['Shanghai']['New Delhi'],'Singapore':cities_distance['Singapore']['Shanghai'],'Tokyo':cities_distance['Tokyo']['Shanghai']},
                'New Delhi':{'Manila':cities_distance['Manila']['New Delhi'],'Shanghai':cities_distance['New Delhi']['Shanghai']}}

KL_WashingtonDC_Route = {'Kuala Lumpur':{'Singapore':cities_distance['Kuala Lumpur']['Singapore'],'New Delhi':cities_distance['Kuala Lumpur']['New Delhi'],'Paris':cities_distance['Kuala Lumpur']['Paris'], 'Manila':cities_distance['Kuala Lumpur']['Manila']},
                    'Singapore':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Singapore'],'Shanghai':cities_distance['Singapore']['Shanghai'],'Tokyo':cities_distance['Singapore']['Tokyo']},
                    'New Delhi':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['New Delhi'],'New York':cities_distance['New Delhi']['New York']},
                    'Paris':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Paris'],'Shanghai':cities_distance['Shanghai']['Paris']},
                    'Shanghai':{'Singapore':cities_distance['Singapore']['Shanghai'],'Manila':cities_distance['Manila']['Shanghai'],'Paris':cities_distance['Shanghai']['Paris'],'Washington DC':cities_distance['Shanghai']['Washington DC']},
                    'Tokyo':{'Singapore':cities_distance['Singapore']['Tokyo'],'Manila':cities_distance['Manila']['Tokyo']},
                    'Manila':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Manila'],'Shanghai':cities_distance['Shanghai']['Manila'],"New York":cities_distance["New York"]["Manila"]},
                    'New York':{'New Delhi':cities_distance['New York']['New Delhi'], 'Manila':cities_distance['New York']['Manila']},
                    'Washington DC':{'Tokyo':cities_distance['Tokyo']['Washington DC'],'Shanghai':cities_distance['Shanghai']['Washington DC'],'New York':cities_distance["New York"]['Washington DC'],"Singapore":cities_distance["Singapore"]["Washington DC"]}}


KL_Shanghai_Route={'Kuala Lumpur':{'Singapore':cities_distance['Kuala Lumpur']['Singapore'],'New Delhi':cities_distance['Kuala Lumpur']['New Delhi'],'Paris':cities_distance['Kuala Lumpur']['Paris'],'Washington DC':cities_distance['Kuala Lumpur']['Washington DC']},
                   'Singapore':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Singapore'],'Manila':cities_distance['Singapore']['Manila'],'Tokyo':cities_distance['Singapore']['Tokyo']},
                   'New Delhi':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['New Delhi'],'New York':cities_distance['New Delhi']["New York"]},
                   'Paris':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Paris'],'Manila':cities_distance['Paris']['Manila']},
                   'Manila':{'Singapore':cities_distance['Singapore']['Manila'],'Shanghai':cities_distance['Shanghai']['Manila']},
                   'Tokyo':{'Singapore':cities_distance['Singapore']['Tokyo'],'Shanghai':cities_distance['Shanghai']['Tokyo']},
                   'Washington DC':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Washington DC'],'Manila':cities_distance['Manila']['Washington DC']},
                   'New York':{'New Delhi':cities_distance['New York']['New Delhi'],'Shanghai':cities_distance['New York']['Shanghai']},
                   'Shanghai':{'Manila':cities_distance['Manila']['Shanghai'],'Washington DC':cities_distance['Washington DC']['Shanghai']}
                   }

KL_Paris_Route={'Kuala Lumpur':{'Singapore':cities_distance['Kuala Lumpur']['Singapore'],'New Delhi':cities_distance['Kuala Lumpur']['New Delhi'],'Shanghai':cities_distance['Kuala Lumpur']['Shanghai'],'Washington DC':cities_distance['Kuala Lumpur']['Washington DC']},
                'Singapore':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Singapore'],'Manila':cities_distance['Singapore']['Manila'],'Tokyo':cities_distance['Singapore']['Tokyo']},
                'New Delhi':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['New Delhi'],'New York':cities_distance['New Delhi']["New York"]},
                'Shanghai':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Shanghai'],'Manila':cities_distance['Shanghai']['Manila']},
                'Manila':{'Singapore':cities_distance['Singapore']['Manila'],'Shanghai':cities_distance['Shanghai']['Manila'],"Paris":cities_distance["Paris"]["Manila"]},
                'Tokyo':{'Singapore':cities_distance['Singapore']['Tokyo'],'Shanghai':cities_distance['Shanghai']['Tokyo']},
                'Washington DC':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Washington DC'],'Manila':cities_distance['Manila']['Washington DC'],"Paris":cities_distance["Paris"]["Washington DC"]},
                'New York':{'New Delhi':cities_distance['New York']['New Delhi'],'Shanghai':cities_distance['New York']['Shanghai']},
                'Paris':{'Manila':cities_distance['Manila']['Paris'],'Washington DC':cities_distance['Washington DC']['Paris']}
                   }

KL_NY_Route={'Kuala Lumpur':{'Singapore':cities_distance['Kuala Lumpur']['Singapore'],'New Delhi':cities_distance['Kuala Lumpur']['New Delhi'],'Shanghai':cities_distance['Kuala Lumpur']['Shanghai']},
             'Singapore':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Singapore'],'Manila':cities_distance['Singapore']['Manila'],'Tokyo':cities_distance['Singapore']['Tokyo']},
             'New Delhi':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['New Delhi'],'Paris':cities_distance['New Delhi']["Paris"]},
             'Shanghai':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Shanghai'],'Manila':cities_distance['Shanghai']['Manila']},
             'Manila':{'Singapore':cities_distance['Singapore']['Manila'],'Shanghai':cities_distance['Shanghai']['Manila'],"New York":cities_distance["New York"]["Manila"]},
             'Tokyo':{'Singapore':cities_distance['Singapore']['Tokyo'],'Shanghai':cities_distance['Shanghai']['Tokyo']},
             'Washington DC':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Washington DC'],'Manila':cities_distance['Manila']['Washington DC'],"New York":cities_distance["New York"]["Washington DC"]},
             'Paris':{'New Delhi':cities_distance['Paris']['New Delhi'],'Shanghai':cities_distance['Paris']['Shanghai']},
             'New York':{'Manila':cities_distance['Manila']['New York'],'Washington DC':cities_distance['Washington DC']['New York']}
                   }

KL_SG_Route={'Kuala Lumpur':{'New York':cities_distance['Kuala Lumpur']['New York'],'New Delhi':cities_distance['Kuala Lumpur']['New Delhi'],'Shanghai':cities_distance['Kuala Lumpur']['Shanghai'],'Washington DC':cities_distance['Kuala Lumpur']['Washington DC']},
             'New York':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['New York'],'Manila':cities_distance['New York']['Manila'],'Tokyo':cities_distance['New York']['Tokyo']},
             'New Delhi':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['New Delhi'],'Paris':cities_distance['New Delhi']["Paris"]},
             'Shanghai':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Shanghai'],'Manila':cities_distance['Shanghai']['Manila']},
             'Manila':{'New York':cities_distance['New York']['Manila'],'Shanghai':cities_distance['Shanghai']['Manila'],'Singapore':cities_distance['Manila']['Singapore']},
             'Tokyo':{'New York':cities_distance['New York']['Tokyo'],'Shanghai':cities_distance['Shanghai']['Tokyo']},
             'Washington DC':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Washington DC'],'Manila':cities_distance['Manila']['Washington DC'],'Singapore':cities_distance['Washington DC']['Singapore']},
             'Paris':{'New Delhi':cities_distance['Paris']['New Delhi'],'Shanghai':cities_distance['Paris']['Shanghai']},
             'Singapore':{'Manila':cities_distance['Manila']['Singapore'],'Washington DC':cities_distance['Washington DC']['Singapore']}
                   }

dest=input("Enter Destination: ")

if dest=="Shanghai":
    dijkstra(KL_Shanghai_Route,"Kuala Lumpur",dest)
elif dest=="Manila":
    dijkstra(KL_Manila_Route,"Kuala Lumpur",dest)
elif dest=="Tokyo":
    dijkstra(KL_Tokyo_Route,"Kuala Lumpur",dest)
elif dest=="New Delhi":
    dijkstra(KL_NewDelhi_Route,"Kuala Lumpur",dest)
elif dest=="Washington DC":
    dijkstra(KL_WashingtonDC_Route,"Kuala Lumpur",dest)
elif dest=="Shanghai":
    dijkstra(KL_Shanghai_Route,"Kuala Lumpur",dest)
elif dest=="Paris":
    dijkstra(KL_Paris_Route,"Kuala Lumpur",dest)
elif dest=="New York":
    dijkstra(KL_NY_Route,"Kuala Lumpur",dest)
else:
    dijkstra(KL_SG_Route,"Kuala Lumpur",dest)




gmap3.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
gmap3.marker(cities_latitude[0],cities_longitude[0],'cornflowerblue')
gmap3.apikey="AIzaSyDmpwQtMwmoWGHX2UBqnAldc8CFDus77RQ"
gmap3.draw("gmap3.html")


end=time.time()




print("Running Time: ",(end-start))
url = "gmap3.html"
webbrowser.open(url,new=2)
