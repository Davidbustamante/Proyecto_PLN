import nltk
import random
from nltk.corpus import gutenberg

TEXT = nltk.words('prueba.txt')

# NLTK shortcuts :)
bigrams = NLTK.bigrams(TEXT)
cfd = nltk.ConditionalFreqDist(bigrams)

# pick a random word from the corpus to start with
word = random.choice(TEXT)
# generate 15 more words
for i in range(40):
    #print word,
    if word in cfd:
        word = random.choice(cfd[word].keys())
    else:
        break