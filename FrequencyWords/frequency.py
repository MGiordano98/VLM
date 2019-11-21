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
            t = text.split()
            if t[1].endswith(':'):
                x.append(t[1])
    wow = getMethods.getRslt(x)
    words.append(wow)


for i,val in enumerate(hashtags):
    print("\n")
    print(val)
    print(words[i])


