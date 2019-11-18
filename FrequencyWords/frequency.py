from collections import Counter
import pandas as pd
import nltk
import re
import getMethods

hashtags = getMethods.getHashtags()

tweets = getMethods.getTweets()

tweets_RT = {}
tweets_NoRT = {}

for i,val in enumerate(hashtags):
    tweets[val] = tweets[val].drop_duplicates(subset='text', keep='first')


""" 
for key,value in tweets.items():
    x = []
    y = []
    for text in value["text"]:
        if 'RT @' in text:
            x.append(text)
        else:
            y.append(tweets[key]["screen_name"])
    tweets_RT[key] = x
    tweets_NoRT[key] = y
 """


stopwords_it = nltk.corpus.stopwords.words('italian')
stopwords_en = nltk.corpus.stopwords.words('english')
stopwords = stopwords_it + stopwords_en
RE_stopwords = r'\b(?:{})\b'.format('|'.join(stopwords))



words =  {}


""" for i,val in enumerate(hashtags):
    x = []
    for t in tweets_NoRT[val]:
        for i in t.split():
            if i.startswith('@'):
                x.append(i)
    wow = getMethods.getRslt(x)
    words[val] = wow """
""" 
print(tweets_NoRT)
for key,value in enumerate(tweets_NoRT[val]):
    print(key)


for i,val in enumerate(hashtags):
    print(words[val]) """




for i,val in enumerate(hashtags):
    x = []
    for t in tweets[val]["text"]:
        for i in t.split():
            if i.startswith('@'):
                x.append(i)
    wow = getMethods.getRslt(x)
    words[val] = wow



for key,value in words.items():
    print(value.head(5))
