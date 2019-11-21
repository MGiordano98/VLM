from collections import Counter
import pandas as pd
import nltk
import re
import getMethods

hashtags = getMethods.getHashtags()

tweets= getMethods.getTweets()

words = []

for key,value in tweets.items():
    x = []
    for text in value["text"]:
        if 'RT @' in text:
            x.append(text)
        else:
            y.append(tweets[key]["screen_name"])
    tweets_RT[key] = x
    tweets_NoRT[key] = y
 


stopwords_it = nltk.corpus.stopwords.words('italian')
stopwords_en = nltk.corpus.stopwords.words('english')
stopwords = stopwords_it + stopwords_en
RE_stopwords = r'\b(?:{})\b'.format('|'.join(stopwords))



words =  {}
wordsRT = {}
dizionario = {}
for key,value in tweets_RT.items():
    x = []
    for t in value:
        y = t.split()
        x.append(y[1])
    wow = getMethods.getRslt(x)
    wordsRT[key] = wow

""" for i,val in enumerate(hashtags):
    x = []
    for t in tweetsoRT[val]:
        for i in t.split():
            if i.startswith('@'):
                x.append(i)
    wow = getMethods.getRslt(x)
    words.append(wow)


for i,val in enumerate(hashtags):
    print(words[val]) """



for i,val in enumerate(hashtags):
    x = []
    for t in tweets[val]["text"]:
        for i in t.split():
            if i.startswith('@') and not i.endswith(':'):
                x.append(i)
    wow = getMethods.getRslt(x)
    words[val] = wow


print("Generale")
for key,value in words.items():
    print("\n")
    print(key)
    print(value.head(5))
print("\n\n")

print("RT")
for key,value in wordsRT.items():
    print("\n")
    print(key)
    print(value.head(5))
