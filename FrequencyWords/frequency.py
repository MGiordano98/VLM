from collections import Counter
import pandas as pd
import nltk
import re
import getMethods

hashtags = getMethods.getHashtags()

tweets= getMethods.getTweets()

for i,val in enumerate(hashtags):
    tweets[val] = tweets[val].drop_duplicates(subset='text', keep='first')


stopwords_it = nltk.corpus.stopwords.words('italian')
stopwords_en = nltk.corpus.stopwords.words('english')
stopwords = stopwords_it + stopwords_en
RE_stopwords = r'\b(?:{})\b'.format('|'.join(stopwords))


words_nutella_biscuits = []
words_ABH = []

words = []


for i,val in enumerate(hashtags):
    x = []
    for t in tweets[val]["text"]:
        for i in t.split():
            if i.startswith('@'):
                x.append(i)
    wow = getMethods.getRslt(x)
    words.append(wow)


for i,val in enumerate(hashtags):
    print(val)
    print(words[i])