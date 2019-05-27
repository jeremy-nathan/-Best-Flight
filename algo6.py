import nltk
import string
import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome. The sky is pinkish-blue. You shouldn't eat cardboard"""
punctuation = """!\"#$%&()*+/:;<=>?@[\\]^_`{|}~,."""
# tokenized_text=sent_tokenize(text)
# print(tokenized_text)
nltk.download('punkt')
from nltk.tokenize import word_tokenize
# tokenizer = RegexpTokenizer(r'\w+')
# tokenized_word = tokenizer.tokenize(text)
# tokenized_word = text.translate(string.punctuation)
# tokenized_word = re.sub('\W+',' ',text)
# tokenized_word=word_tokenize(text
tokenized_word = ""
for i in text:
    if i not in punctuation:
        tokenized_word += i
print("Tokenized word")
print(tokenized_word)

filestop = open("stopwords.txt")
stopline = filestop.read()
stopwordsnew = stopline.split( )

from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
print(fdist)

print(fdist.most_common(2))



from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
print(stop_words)

import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()
# tokenized_word.split( )
tokenized_word = tokenized_word.lower()
filtered_sent=[]
for w in tokenized_word.split():
    if w not in stopwordsnew:
        filtered_sent.append(w)
        print(filtered_sent)
tokenized_word = tokenized_word.split(" ")
print("Tokenized Sentence:",tokenized_word)
print("Filtered Sentence:",filtered_sent)
