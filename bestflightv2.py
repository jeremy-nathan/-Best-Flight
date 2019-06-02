import geopy
from geopy.geocoders import Nominatim
from geopy import distance
import gmplot
import time
import random
start=time.time()
import webbrowser
from itertools import combinations
import string
import re


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


sent_cities=['Shanghai','New York','Singapore','New Delhi','Washington DC','Tokyo','Paris','Manila']

ratpositivenegative = []
positiveword = []
negativeword = []

def calculateposandneg(cities):
    for x in cities:
        file1 = open(x+".txt")
        line = file1.read()# Use this to read file content as a stream:
        words = line.split()
        # print(words)
        allow = string.ascii_letters + string.digits
        re.sub('[^%s]]' % allow, '', line)
        table = str.maketrans({key: None for key in string.punctuation})
        new_s = line.translate(table)

        print("Words with punctuation of "+x+ " articles : " + line)
        print('\n')
        print("Words without punctuation "+x+ " articles : "+ new_s)
        print('\n')

        # tokenized_text=sent_tokenize(text)
        # print(tokenized_text)

        new_s = new_s.lower()
        from nltk.tokenize import word_tokenize
        tokenized_word=word_tokenize(new_s)
        # print(tokenized_word)
        print('\n')



        from nltk.corpus import stopwords
        stop_words=set(stopwords.words("english"))
        print(stop_words)
        print('\n')

        filtered_sent=[]
        for w in tokenized_word:
            if w not in stop_words:
                filtered_sent.append(w)

        stopwords_sent = []
        for y in tokenized_word:
            if y in stop_words:
                stopwords_sent.append(y)

        print("Tokenized Sentence:",tokenized_word)
        print('\n')
        print("Filterd Sentence:",filtered_sent)
        print('\n')
        print("Stopword Sentence:",stopwords_sent)
        print('\n')
        from nltk.probability import FreqDist
        fdist = FreqDist(filtered_sent)
        fdist1 = FreqDist(stopwords_sent)
        print(fdist)
        print('\n')
        print("Most Common word :",fdist.most_common(2))
        print('\n')
        print("Most Common Stopword :",fdist1.most_common(2))

        # import matplotlib.pyplot as plt
        # plt.xlabel('Count Words')
        # plt.ylabel('Frequency')
        # plt.title('The Frequency of Count Words for : '+x+" articles")
        # fdist.plot(30,cumulative=False)
        #
        # plt.show()
        #
        #
        # import matplotlib.pyplot as plt1
        # plt1.xlabel('Stop Words')
        # plt1.ylabel('Frequency')
        # plt1.title('The Frequency of Stop Words for : '+x+" articles")
        # fdist1.plot(30,cumulative=False)
        #
        # plt1.show()




        appendFile = open('filteredtext1.txt','w')
        for r in filtered_sent:
            appendFile.write(" "+r)

        appendFile.close()

        file1 = open("filteredtext1.txt")
        theTweet = file1.read()  # Use this to read file content as a stream:

        file2 = open("positive.txt")
        line2 = file2.read()  # Use this to read file content as a stream:
        positive_words = line2.split(", ")

        file3 = open("negative.txt")
        line3 = file3.read()  # Use this to read file content as a stream:
        negative_words = line3.split(", ")



        theTokens = re.findall(r'\b\w[\w-]*\b', theTweet)
        print("The Tokenized Words", theTokens)
        print("\n")

        numPosWords = 0
        numPos = []
        for word in theTokens:
            if word in positive_words:
                numPosWords += 1
                numPos.append(word)

        positiveword.append(numPosWords)

        print("Total number of Positive Words: ", numPosWords)
        print("The Positive words for article "+x+" :", numPos)
        # numposcities = numPosWords
        numNegWords = 0
        numNeg = []
        for words in theTokens:
            if words in negative_words:
                numNegWords += 1
                numNeg.append(words)
        # print()
        # print("Total number of Negative Words: ", numNegWords)
        # print("The Negative Words for article "+x+" :", numNeg)
        negativeword.append(numNegWords)
        numWords = len(theTokens)
        print(numWords)
        percntPos = numPosWords / numWords
        percntNeg = numNegWords / numWords
        print()
        print("Positive: " + "{:.0%}".format(percntPos) + "  Negative: " + "{:.0%}".format(percntNeg))
        print()
        if numPosWords > numNegWords:
            print("Positive " + str(numPosWords) + ":" + str(numNegWords))
            print()
            print("The Article has a Positive Sentimental Analysis!!!!")
        elif numNegWords > numPosWords:
            print("Negative " + str(numPosWords) + ":" + str(numNegWords))
            print()
            print("The Article has a Negative Sentimental Analysis!!!!")
        elif numNegWords == numPosWords:
            print("Neutral " + str(numPosWords) + ":" + str(numNegWords))
            print()
            print("The Article has a Neutral Sentimental Analysis!!!!")

difposneg = []
calculateposandneg(sent_cities)
for i in range(len(positiveword)):
    difposneg.append(positiveword[i]-negativeword[i])

cities_distance['Kuala Lumpur']['Singapore'] -= difposneg[2]


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
        # print(path_latitude)


        for i in range (len(cities_coords)):
              gmap3.plot(path_latitude,path_longitude,'red', edge_width = 3.0)

        return path
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
        return dijkstra(graph,x,dest,visited,distances,predecessors)

KL_Manila_Route = {'Kuala Lumpur':{'Singapore':(cities_distance['Kuala Lumpur']['Singapore']-difposneg[2]),'New Delhi':cities_distance['Kuala Lumpur']['New Delhi']-difposneg[3],'Paris':cities_distance['Kuala Lumpur']['Paris']-difposneg[6], 'Washington DC':cities_distance['Kuala Lumpur']['Washington DC']-difposneg[4]},
                    'Singapore':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Singapore']-difposneg[2],'Shanghai':cities_distance['Singapore']['Shanghai']-(difposneg[2]-difposneg[0]),'Tokyo':cities_distance['Singapore']['Tokyo']-(difposneg[2]-difposneg[5])},
                    'New Delhi':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['New Delhi']-difposneg[3],'New York':cities_distance['New Delhi']['New York']-(difposneg[3]-difposneg[1])},
                    'Paris':{'Kuala Lumpur':cities_distance['Kuala Lumpur']['Paris']-difposneg[6],'Shanghai':cities_distance['Shanghai']['Paris']},
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
# dijkstra(KL_NY_Route,"Kuala Lumpur",dest)

if dest=="Shanghai":
    a=dijkstra(KL_Shanghai_Route,"Kuala Lumpur",dest)
elif dest=="Manila":
    a=dijkstra(KL_Manila_Route,"Kuala Lumpur",dest)
elif dest=="Tokyo":
    a=dijkstra(KL_Tokyo_Route,"Kuala Lumpur",dest)
elif dest=="New Delhi":
    a=dijkstra(KL_NewDelhi_Route,"Kuala Lumpur",dest)
elif dest=="Washington DC":
    a=dijkstra(KL_WashingtonDC_Route,"Kuala Lumpur",dest)
elif dest=="Shanghai":
    a=dijkstra(KL_Shanghai_Route,"Kuala Lumpur",dest)
elif dest=="Paris":
    a=dijkstra(KL_Paris_Route,"Kuala Lumpur",dest)
elif dest=="New York":
    a=dijkstra(KL_NY_Route,"Kuala Lumpur",dest)
else:
    a=dijkstra(KL_SG_Route,"Kuala Lumpur",dest)




gmap3.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
gmap3.marker(cities_latitude[0],cities_longitude[0],'cornflowerblue')
gmap3.apikey="AIzaSyDmpwQtMwmoWGHX2UBqnAldc8CFDus77RQ"
gmap3.draw("gmap3.html")


end=time.time()




print("Running Time: ",(end-start))
url = "gmap3.html"
webbrowser.open(url,new=2)




import nltk
from nltk.tokenize import sent_tokenize
import string
import re
import winsound
name = [a[1],a[2]]
length = len(name)

for x in name:
    file1 = open(x+".txt")
    line = file1.read()# Use this to read file content as a stream:
    words = line.split()
    # print(words)
    allow = string.ascii_letters + string.digits
    re.sub('[^%s]]' % allow, '', line)
    table = str.maketrans({key: None for key in string.punctuation})
    new_s = line.translate(table)

    print("Words with punctuation of "+x+ " articles : " + line)
    print('\n')
    print("Words without punctuation "+x+ " articles : "+ new_s)
    print('\n')

    # tokenized_text=sent_tokenize(text)
    # print(tokenized_text)

    new_s = new_s.lower()
    from nltk.tokenize import word_tokenize
    tokenized_word=word_tokenize(new_s)
    # print(tokenized_word)
    print('\n')



    from nltk.corpus import stopwords
    stop_words=set(stopwords.words("english"))
    print(stop_words)
    print('\n')

    filtered_sent=[]
    for w in tokenized_word:
        if w not in stop_words:
            filtered_sent.append(w)

    stopwords_sent = []
    for y in tokenized_word:
        if y in stop_words:
            stopwords_sent.append(y)

    print("Tokenized Sentence:",tokenized_word)
    print('\n')
    print("Filterd Sentence:",filtered_sent)
    print('\n')
    print("Stopword Sentence:",stopwords_sent)
    print('\n')
    from nltk.probability import FreqDist
    fdist = FreqDist(filtered_sent)
    fdist1 = FreqDist(stopwords_sent)
    print(fdist)
    print('\n')
    print("Most Common word :",fdist.most_common(2))
    print('\n')
    print("Most Common Stopword :",fdist1.most_common(2))

    import matplotlib.pyplot as plt
    plt.xlabel('Count Words')
    plt.ylabel('Frequency')
    plt.title('The Frequency of Count Words for : '+x+" articles")
    fdist.plot(30,cumulative=False)

    plt.show()


    import matplotlib.pyplot as plt1
    plt1.xlabel('Stop Words')
    plt1.ylabel('Frequency')
    plt1.title('The Frequency of Stop Words for : '+x+" articles")
    fdist1.plot(30,cumulative=False)

    plt1.show()




    appendFile = open('filteredtext1.txt','w')
    for r in filtered_sent:
        appendFile.write(" "+r)

    appendFile.close()

    file1 = open("filteredtext1.txt")
    theTweet = file1.read()  # Use this to read file content as a stream:

    file2 = open("positive.txt")
    line2 = file2.read()  # Use this to read file content as a stream:
    positive_words = line2.split(", ")

    file3 = open("negative.txt")
    line3 = file3.read()  # Use this to read file content as a stream:
    negative_words = line3.split(", ")

    import re

    theTokens = re.findall(r'\b\w[\w-]*\b', theTweet)
    print("The Tokenized Words", theTokens)
    print("\n")

    numPosWords = 0
    numPos = []
    for word in theTokens:
        if word in positive_words:
            numPosWords += 1
            numPos.append(word)

    print("Total number of Positive Words: ", numPosWords)
    print("The Positive words for article "+x+" :", numPos)

    numNegWords = 0
    numNeg = []
    for words in theTokens:
        if words in negative_words:
            numNegWords += 1
            numNeg.append(words)
    print()
    print("Total number of Negative Words: ", numNegWords)
    print("The Negative Words for article "+x+" :", numNeg)

    numWords = len(theTokens)
    print(numWords)
    percntPos = numPosWords / numWords
    percntNeg = numNegWords / numWords
    print()
    print("Positive: " + "{:.0%}".format(percntPos) + "  Negative: " + "{:.0%}".format(percntNeg))
    print()
    if numPosWords > numNegWords:
        print("Positive " + str(numPosWords) + ":" + str(numNegWords))
        print()
        print("The Article has a Positive Sentimental Analysis!!!!")
    elif numNegWords > numPosWords:
        print("Negative " + str(numPosWords) + ":" + str(numNegWords))
        print()
        print("The Article has a Negative Sentimental Analysis!!!!")
    elif numNegWords == numPosWords:
        print("Neutral " + str(numPosWords) + ":" + str(numNegWords))
        print()
        print("The Article has a Neutral Sentimental Analysis!!!!")

    print()

    appendFile = open('Positive_InText_'+x+'.txt', 'w')
    for j in numPos:
        appendFile.write(j + ", ")

    appendFile.close()

    appendFile = open('Negative_InText_'+x+'.txt', 'w')
    for z in numNeg:
        appendFile.write(z + ", ")

    appendFile.close()

    import seaborn as sns

    sns.set_style("whitegrid")
    import matplotlib.pyplot as plt

    values = [percntPos * 100, percntNeg * 100]
    labels1 = ["Positive", "Negative"]
    cols = ['c', 'r']
    plt.pie(values, labels=labels1, colors=cols, autopct='%1.1f%%')


    plt.title('The Percentage of Positive and Negative Sentiment of The '+x+" Article" )
    plt.legend()
    plt.show()
    x = [1, 2]
    y = [numPosWords,numNegWords]
    labels = ["Positive","Negative"]

    plt.bar(x, y, align='center')
    plt.xticks(x, labels)
    plt.title('The Total of Positive and Negative Sentiment of Article')
    plt.ylabel("Total Words")
    plt.show()

    winsound.PlaySound("Sound", winsound.SND_FILENAME)

def AnalaysisArticle(positive, negative, neutral, fullword, dic):
    freq = getFreq(positive, negative, neutral, fullword, dic)
    percent = getPercent(freq["Positive"], freq["Negative"], freq["Neutral"], freq["Full"])
    results = {"freq": freq, "percent": percent}
    return results




def AnalysisFreq(percent):
    print ("Article is", max(percent, key=lambda i: percent[i]))

def getPercent(pos, neg, neut, full):
    ratio = 100/full
    percent = {
    "Positive": pos*ratio,
    "Negative": neg*ratio,
    "Neutral": neut*ratio

    }
    return percent

def getFreq(pos, neg, neut, full, dic):
    pos = 0
    neg = 0
    neut = 0
    full = 0

    for i in pos:
        pos += dic[i]
    for i in neg:
        neg += dic[i]
    for i in neut:
        neut += dic[i]
    for i in dic.keys():
        full += dic[i]
    freq = {
    "Positive": pos, "Negative": neg, "Neutral": neut, "Full": full
    }
    return freq

def get_dic(keys, ori_dic):
    new_dic = {}
    for i in keys:
        new_dic[i] = ori_dic[i]
    return new_dic

def printAnalysis(results):
    table_header = ["Type","Total Words", "Percentage (%)"]
    table_body = [
    ["Positive", results["freq"]["Positive"], "%.f" % results["percent"]["Positive"]],
    ["Negative", results["freq"]["Negative"], "%.f" % results["percent"]["Negative"]],
    ["Neutral", results["freq"]["Neutral"], "%.f" % results["percent"]["Neutral"]]
    ]

    print (tabulate(table_body, table_header), "\n\nTotal Words: ", results["freq"]["Full"])
    AnalysisFreq(results["percent"])


    if pos > neg:
        print("The country has positive sentiment. ")

    elif neg > pos:
        print("The country has negative sentiment. ")

    elif neg == pos:
        print("The country has natural sentiment.")





    # winsound.PlaySound("Sound", winsound.SND_FILENAME)


    from gtts import gTTS
    text="Thank You"
    speech = gTTS(text,'en')
    speech.save("Bye.mp3")

import os
os.startfile('Bye.mp3')
