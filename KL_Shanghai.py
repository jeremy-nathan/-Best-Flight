import geopy
from geopy.geocoders import Nominatim
from geopy import distance
import gmplot
import time
# from djikstras import A
import random
start=time.time()
import webbrowser
from itertools import combinations
#import location_markers.py

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
print(comb_distance[0])

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


KL_Sing_Manila  = {"Kuala Lumpur":{"Singapore":cities_distance['Kuala Lumpur']['Singapore']},
                    "Singapore":{"Kuala Lumpur":cities_distance['Kuala Lumpur']['Singapore'],"Tokyo":cities_distance['Singapore']['Tokyo'],"New York":cities_distance['Singapore']['New York'],'Shanghai':cities_distance['Singapore']['Shanghai'],'Washington DC':cities_distance['Singapore']['Washington DC'],'Paris':cities_distance['Singapore']['Paris'],
                    'New Delhi':cities_distance['Singapore']['New Delhi']},
                    "Tokyo":{"Singapore":cities_distance['Tokyo']['Singapore'],"Manila":cities_distance['Tokyo']['Manila']},
                    "New York":{"Singapore":cities_distance['New York']['Singapore'],"Manila":cities_distance['New York']['Manila']},
                    "Shanghai":{"Singapore":cities_distance['Shanghai']['Singapore'],"Manila":cities_distance['Shanghai']['Manila']},
                    "Washington DC" :{"Singapore":cities_distance['Washington DC']['Singapore'],"Manila":cities_distance['Washington DC']['Manila']},
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       }

KL_Tokyo_Manila = {"Kuala Lumpur":{"Tokyo":cities_distance['Kuala Lumpur']['Tokyo']},
                    "Tokyo":{"Kuala Lumpur":cities_distance['Kuala Lumpur']['Tokyo'],"Singapore":cities_distance['Singapore']['Tokyo'],"New York":cities_distance['Tokyo']['New York'],'Shanghai':cities_distance['Tokyo']['Shanghai'],'Washington DC':cities_distance['Tokyo']['Washington DC'],'Paris':cities_distance['Paris']['Tokyo'],
                    'New Delhi':cities_distance['Tokyo']['New Delhi']},
                    "Singapore":{"Tokyo":cities_distance['Tokyo']['Singapore'],"Manila":cities_distance['Singapore']['Manila']},
                    "New York":{"Tokyo":cities_distance['New York']['Tokyo'],"Manila":cities_distance['New York']['Manila']},
                    "Shanghai":{"Tokyo":cities_distance['Shanghai']['Tokyo'],"Manila":cities_distance['Shanghai']['Manila']},
                    "Washington DC" :{"Tokyo":cities_distance['Washington DC']['Tokyo'],"Manila":cities_distance['Washington DC']['Manila']},
                    "Paris":{"Tokyo":cities_distance['Paris']['Tokyo'],"Manila":cities_distance['Paris']['Manila']},
                    "New Delhi":{"Tokyo":cities_distance['New Delhi']['Tokyo'],"Manila":cities_distance['New Delhi']['Manila']},
                    "Manila":{"Singapore":cities_distance["Singapore"]["Manila"],"New York":cities_distance["New York"]["Manila"],"Shanghai":cities_distance["Shanghai"]["Manila"],"Washington DC":cities_distance["Washington DC"]["Manila"],"Paris":cities_distance["Paris"]["Manila"],"New Delhi":cities_distance["New Delhi"]["Manila"]}
                     }

KL_WashingtonDC_Manila = {"Kuala Lumpur":{"Washington DC":cities_distance['Kuala Lumpur']['Washington DC']},
                    "Washington DC":{"Kuala Lumpur":cities_distance['Kuala Lumpur']['Washington DC'],"Tokyo":cities_distance['Washington DC']['Tokyo'],"New York":cities_distance['Washington DC']['New York'],'Shanghai':cities_distance['Washington DC']['Shanghai'],'Singapore':cities_distance['Singapore']['Washington DC'],'Paris':cities_distance['Washington DC']['Paris'],
                    'New Delhi':cities_distance['Washington DC']['New Delhi']},
                    "Tokyo":{"Washington DC":cities_distance['Tokyo']['Washington DC'],"Manila":cities_distance['Tokyo']['Manila']},
                    "New York":{"Washington DC":cities_distance['New York']['Washington DC'],"Manila":cities_distance['New York']['Manila']},
                    "Shanghai":{"Washington DC":cities_distance['Shanghai']['Washington DC'],"Manila":cities_distance['Shanghai']['Manila']},
                    "Singapore" :{"Washington DC":cities_distance['Washington DC']['Singapore'],"Manila":cities_distance['Singapore']['Manila']},
                    "Paris":{"Washington DC":cities_distance['Paris']['Washington DC'],"Manila":cities_distance['Paris']['Manila']},
                    "New Delhi":{"Washington DC":cities_distance['New Delhi']['Washington DC'],"Manila":cities_distance['New Delhi']['Manila']},
                    "Manila":{"Tokyo":cities_distance["Tokyo"]["Manila"],"New York":cities_distance["New York"]["Manila"],"Shanghai":cities_distance["Shanghai"]["Manila"],"Singapore":cities_distance["Singapore"]["Manila"],"Paris":cities_distance["Paris"]["Manila"],"New Delhi":cities_distance["New Delhi"]["Manila"]}
                     }

KL_NewDelhi_Manila = {"Kuala Lumpur":{"New Delhi":cities_distance['Kuala Lumpur']['New Delhi']},
                    "New Delhi":{"Kuala Lumpur":cities_distance['Kuala Lumpur']['New Delhi'],"Tokyo":cities_distance['New Delhi']['Tokyo'],"New York":cities_distance['New Delhi']['New York'],'Shanghai':cities_distance['New Delhi']['Shanghai'],'Washington DC':cities_distance['New Delhi']['Washington DC'],'Paris':cities_distance['New Delhi']['Paris'],
                    'Singapore':cities_distance['Singapore']['New Delhi']},
                    "Tokyo":{"New Delhi":cities_distance['Tokyo']['New Delhi'],"Manila":cities_distance['Tokyo']['Manila']},
                    "New York":{"New Delhi":cities_distance['New York']['New Delhi'],"Manila":cities_distance['New York']['Manila']},
                    "Shanghai":{"New Delhi":cities_distance['Shanghai']['New Delhi'],"Manila":cities_distance['New Delhi']['Manila']},
                    "Washington DC" :{"New Delhi":cities_distance['Washington DC']['New Delhi'],"Manila":cities_distance['Washington DC']['Manila']},
                    "Paris":{"New Delhi":cities_distance['Paris']['New Delhi'],"Manila":cities_distance['Paris']['Manila']},
                    "Singapore":{"New Delhi":cities_distance['New Delhi']['Singapore'],"Manila":cities_distance['Singapore']['Manila']},
                    "Manila":{"Tokyo":cities_distance["Tokyo"]["Manila"],"New York":cities_distance["New York"]["Manila"],"Shanghai":cities_distance["Shanghai"]["Manila"],"Washington DC":cities_distance["Washington DC"]["Manila"],"Paris":cities_distance["Paris"]["Manila"],"Singapore":cities_distance["Singapore"]["Manila"]}
                    }

KL_Shanghai_Manila = {"Kuala Lumpur":{"Shanghai":cities_distance['Kuala Lumpur']['Shanghai']},
                    "Shanghai":{"Kuala Lumpur":cities_distance['Kuala Lumpur']['Shanghai'],"Tokyo":cities_distance['Shanghai']['Tokyo'],"New York":cities_distance['Shanghai']['New York'],'Singapore':cities_distance['Singapore']['Shanghai'],'Washington DC':cities_distance['Shanghai']['Washington DC'],'Paris':cities_distance['Shanghai']['Paris'],
                    'New Delhi':cities_distance['Shanghai']['New Delhi']},
                    "Tokyo":{"Shanghai":cities_distance['Tokyo']['Shanghai'],"Manila":cities_distance['Tokyo']['Manila']},
                    "New York":{"Shanghai":cities_distance['New York']['Shanghai'],"Manila":cities_distance['New York']['Manila']},
                    "Singapore":{"Shanghai":cities_distance['Singapore']['Shanghai'],"Manila":cities_distance['Singapore']['Manila']},
                    "Washington DC" :{"Shanghai":cities_distance['Washington DC']['Shanghai'],"Manila":cities_distance['Washington DC']['Manila']},
                    "Paris":{"Shanghai":cities_distance['Paris']['Shanghai'],"Manila":cities_distance['Paris']['Manila']},
                    "New Delhi":{"Shanghai":cities_distance['New Delhi']['Shanghai'],"Manila":cities_distance['New Delhi']['Manila']},
                    "Manila":{"Tokyo":cities_distance["Tokyo"]["Manila"],"New York":cities_distance["New York"]["Manila"],"Shanghai":cities_distance["Shanghai"]["Manila"],"Washington DC":cities_distance["Washington DC"]["Manila"],"Paris":cities_distance["Paris"]["Manila"],"New Delhi":cities_distance["New Delhi"]["Manila"]}
                     }


KL_Paris_Manila = {"Kuala Lumpur":{"Paris":cities_distance['Kuala Lumpur']['Paris']},
                    "Paris":{"Kuala Lumpur":cities_distance['Kuala Lumpur']['Paris'],"Tokyo":cities_distance['Paris']['Tokyo'],"New York":cities_distance['Paris']['New York'],'Shanghai':cities_distance['Paris']['Shanghai'],'Washington DC':cities_distance['Paris']['Washington DC'],'Singapore':cities_distance['Singapore']['Paris'],
                    'New Delhi':cities_distance['Paris']['New Delhi']},
                    "Tokyo":{"Paris":cities_distance['Tokyo']['Paris'],"Manila":cities_distance['Tokyo']['Manila']},
                    "New York":{"Paris":cities_distance['New York']['Paris'],"Manila":cities_distance['New York']['Manila']},
                    "Shanghai":{"Paris":cities_distance['Shanghai']['Paris'],"Manila":cities_distance['Shanghai']['Manila']},
                    "Washington DC" :{"Paris":cities_distance['Washington DC']['Paris'],"Manila":cities_distance['Washington DC']['Manila']},
                    "Singapore":{"Paris":cities_distance['Paris']['Singapore'],"Manila":cities_distance['Paris']['Manila']},
                    "New Delhi":{"Paris":cities_distance['New Delhi']['Singapore'],"Manila":cities_distance['New Delhi']['Manila']},
                    "Manila":{"Tokyo":cities_distance["Tokyo"]["Manila"],"New York":cities_distance["New York"]["Manila"],"Shanghai":cities_distance["Shanghai"]["Manila"],"Washington DC":cities_distance["Washington DC"]["Manila"],"Singapore":cities_distance["Singapore"]["Manila"],"New Delhi":cities_distance["New Delhi"]["Manila"]}
                     }

KL_NewYork_Manila = {"Kuala Lumpur":{"New York":cities_distance['Kuala Lumpur']['New York']},
                    "New York":{"Kuala Lumpur":cities_distance['Kuala Lumpur']['New York'],"Tokyo":cities_distance['New York']['Tokyo'],"Singapore":cities_distance['New York']['Singapore'],'Shanghai':cities_distance['New York']['Shanghai'],'Washington DC':cities_distance['New York']['Washington DC'],'Paris':cities_distance['New York']['Paris'],
                    'New Delhi':cities_distance['New York']['New Delhi']},
                    "Tokyo":{"New York":cities_distance['Tokyo']['New York'],"Manila":cities_distance['Tokyo']['Manila']},
                    "Singapore":{"New York":cities_distance['New York']['Singapore'],"Manila":cities_distance['Singapore']['Manila']},
                    "Shanghai":{"Singapore":cities_distance['Shanghai']['Paris'],"Manila":cities_distance['Shanghai']['Manila']},
                    "Washington DC" :{"New York":cities_distance['Washington DC']['New York'],"Manila":cities_distance['Washington DC']['Manila']},
                    "Paris":{"New York":cities_distance['Paris']['New York'],"Manila":cities_distance['Paris']['Manila']},
                    "New Delhi":{"New York":cities_distance['New Delhi']['New York'],"Manila":cities_distance['New Delhi']['Manila']},
                    "Manila":{"Tokyo":cities_distance["Tokyo"]["Manila"],"New York":cities_distance["New York"]["Manila"],"Shanghai":cities_distance["Shanghai"]["Manila"],"Washington DC":cities_distance["Washington DC"]["Manila"],"Paris":cities_distance["Paris"]["Manila"],"New Delhi":cities_distance["New Delhi"]["Manila"]}
                     }








KL_Manila_Route = {'Kuala Lumpur':{'Singapore':cities_distance['Kuala Lumpur']['Singapore'],'New Delhi':cities_distance['Kuala Lumpur']['New Delhi'],'Paris':cities_distance['Kuala Lumpur']['Paris'], 'Washington DC':cities_distance['Kuala Lumpur']['Washington DC']},
                    'Singapore':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Singapore'],'Shanghai':cities_distance['Singapore']['Shanghai'],'Tokyo':cities_distance['Singapore']['Tokyo']},
                    'New Delhi':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['New Delhi'],'New York':cities_distance['New Delhi']['New York']},
                    'Paris':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Paris'],'Shanghai':cities_distance['Shanghai']['Paris']},
                    'Shanghai':{'Singapore':cities_distance['Singapore']['Shanghai'],'Manila':cities_distance['Manila']['Shanghai'],'Paris':cities_distance['Shanghai']['Paris'],'Washington DC':cities_distance['Shanghai']['Washington DC']},
                    'Tokyo':{'Singapore':cities_distance['Singapore']['Tokyo'],'Manila':cities_distance['Manila']['Tokyo']},
                    'Washington DC':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Washington DC'],'Shanghai':cities_distance['Shanghai']['Washington DC']},
                    'New York':{'New Delhi':cities_distance['New York']['New Delhi'], 'Manila':cities_distance['New York']['Manila']},
                    'Manila':{'Tokyo':cities_distance['Tokyo']['Manila'],'Shanghai':cities_distance['Shanghai']['Manila'],'New York':cities_distance["New York"]['Manila']}}

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

KL_WashingtonDC_Route = {'Kuala Lumpur':{'New Delhi':cities_distance['Kuala Lumpur']['New Delhi'],'Singapore':cities_distance['Kuala Lumpur']['Singapore'],'Tokyo':cities_distance['Kuala Lumpur']['Tokyo'], 'Paris':cities_distance['Paris']['Kuala Lumpur']},
                'Singapore':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Singapore'],'Manila':cities_distance['Singapore']['Manila'],'Shanghai':cities_distance['Singapore']['Shanghai']},
                'Tokyo':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Tokyo'], 'Shanghai':cities_distance['Shanghai']['Tokyo']},
                'Paris':{'Kuala Lumpur':cities_distance['Paris']['Kuala Lumpur'],'Manila':cities_distance['Paris']['Manila']},
                'New Delhi':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['New Delhi'],'Manila':cities_distance['New Delhi']['Manila']},
                'Manila':{'Paris':cities_distance['Paris']['Manila'],'Washington DC':cities_distance['Washington DC']['Manila'], 'Singapore':cities_distance['Manila']['Singapore'],'Tokyo':cities_distance['Manila']['Tokyo']},
                'Shanghai':{'New Delhi':cities_distance['Shanghai']['New Delhi'],'Singapore':cities_distance['Singapore']['Shanghai'],'Tokyo':cities_distance['Tokyo']['Shanghai']},
                'Washington DC':{'Manila':cities_distance['Manila']['Washington DC'],'Shanghai':cities_distance['Washington DC']['Shanghai']}}


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
                'Manila':{'Singapore':cities_distance['Singapore']['Manila'],'Shanghai':cities_distance['Shanghai']['Manila']},
                'Tokyo':{'Singapore':cities_distance['Singapore']['Tokyo'],'Shanghai':cities_distance['Shanghai']['Tokyo']},
                'Washington DC':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Washington DC'],'Manila':cities_distance['Manila']['Washington DC']},
                'New York':{'New Delhi':cities_distance['New York']['New Delhi'],'Shanghai':cities_distance['New York']['Shanghai']},
                'Paris':{'Manila':cities_distance['Manila']['Paris'],'Washington DC':cities_distance['Washington DC']['Paris']}
                   }

KL_NY_Route={'Kuala Lumpur':{'Singapore':cities_distance['Kuala Lumpur']['Singapore'],'New Delhi':cities_distance['Kuala Lumpur']['New Delhi'],'Shanghai':cities_distance['Kuala Lumpur']['Shanghai'],'Washington DC':cities_distance['Kuala Lumpur']['Washington DC']},
             'Singapore':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Singapore'],'Manila':cities_distance['Singapore']['Manila'],'Tokyo':cities_distance['Singapore']['Tokyo']},
             'New Delhi':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['New Delhi'],'Paris':cities_distance['New Delhi']["Paris"]},
             'Shanghai':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Shanghai'],'Manila':cities_distance['Shanghai']['Manila']},
             'Manila':{'Singapore':cities_distance['Singapore']['Manila'],'Shanghai':cities_distance['Shanghai']['Manila']},
             'Tokyo':{'Singapore':cities_distance['Singapore']['Tokyo'],'Shanghai':cities_distance['Shanghai']['Tokyo']},
             'Washington DC':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Washington DC'],'Manila':cities_distance['Manila']['Washington DC']},
             'Paris':{'New Delhi':cities_distance['Paris']['New Delhi'],'Shanghai':cities_distance['Paris']['Shanghai']},
             'New York':{'Manila':cities_distance['Manila']['New York'],'Washington DC':cities_distance['Washington DC']['New York']}
                   }

KL_SG_Route={'Kuala Lumpur':{'New York':cities_distance['Kuala Lumpur']['New York'],'New Delhi':cities_distance['Kuala Lumpur']['New Delhi'],'Shanghai':cities_distance['Kuala Lumpur']['Shanghai'],'Washington DC':cities_distance['Kuala Lumpur']['Washington DC']},
             'New York':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['New York'],'Manila':cities_distance['New York']['Manila'],'Tokyo':cities_distance['New York']['Tokyo']},
             'New Delhi':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['New Delhi'],'Paris':cities_distance['New Delhi']["Paris"]},
             'Shanghai':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Shanghai'],'Manila':cities_distance['Shanghai']['Manila']},
             'Manila':{'New York':cities_distance['New York']['Manila'],'Shanghai':cities_distance['Shanghai']['Manila']},
             'Tokyo':{'New York':cities_distance['New York']['Tokyo'],'Shanghai':cities_distance['Shanghai']['Tokyo']},
             'Washington DC':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Washington DC'],'Manila':cities_distance['Manila']['Washington DC']},
             'Paris':{'New Delhi':cities_distance['Paris']['New Delhi'],'Shanghai':cities_distance['Paris']['Shanghai']},
             'Singapore':{'Manila':cities_distance['Manila']['Singapore'],'Washington DC':cities_distance['Washington DC']['Singapore']}
                   }


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
        # path_location = [None] *4
        # path_latitude = [None] *4
        # path_longitude = [None] *4
        pred=dest
        #
        #
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        # for i in range(len(path)):
        #     path_location[i] = geolocator.geocode(path[i])
        #     path_latitude[i] = path_location[i].latitude
        #     path_longitude[i] = path_location[i].longitude
        # print(path_latitude)
        #
        #
        # for i in range (len(cities_coords)):
        #       gmap3.plot(path_latitude,path_longitude,'red', edge_width = 3.0)
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

# KL_Manila_route=[KL_Tokyo_Manila,KL_Sing_Manila,KL_WashingtonDC_Manila,KL_NewDelhi_Manila,KL_Shanghai_Manila,KL_Paris_Manila,KL_NewYork_Manila]

# dijkstra(KL_Tokyo_Manila,"Kuala Lumpur","Manila")
# dijkstra(KL_Sing_Manila,"Kuala Lumpur","Manila")

# dijkstra(KL_Tokyo_Manila,"Kuala Lumpur","Manila")
# dijkstra(KL_Sing_Manila,"Kuala Lumpur","Manila")
# dijkstra(KL_WashingtonDC_Manila,"Kuala Lumpur","Manila")
# dijkstra(KL_NewDelhi_Manila,"Kuala Lumpur","Manila")
# dijkstra(KL_Shanghai_Manila,"Kuala Lumpur","Manila")
# dijkstra(KL_Paris_Manila,"Kuala Lumpur","Manila")
dest = "Manila"


dijkstra(KL_Shanghai_Route,"Kuala Lumpur","Shanghai")
