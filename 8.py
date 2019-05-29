import geopy
from geopy.geocoders import Nominatim
from geopy import distance
import gmplot
import time
import random
start=time.time()
import webbrowser
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np
import string
import re

cities=['Shanghai','New York','Singapore','New Delhi','Washington DC','Tokyo','Paris','Manila']

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
        print()
        print("Total number of Negative Words: ", numNegWords)
        print("The Negative Words for article "+x+" :", numNeg)
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
calculateposandneg(cities)
for i in range(len(positiveword)):
    difposneg.append(positiveword[i]-negativeword[i])


plt.title("Probability distribution of passing through each city (Based on political sentiment)" )
plt.legend()
# plt.show()
x = [len(cities)]
y = difposneg
labels = ['Shanghai','New York','Singapore','New Delhi','Washington DC','Tokyo','Paris','Manila']
y_pos = np.arange(len(labels))
plt.bar(labels, y, align='center',alpha =0.5)
plt.xticks(y_pos, labels)
plt.title('The Total of Positive and Negative Sentiment of Article')
plt.ylabel("Difference of positive and negative words")
plt.show()
