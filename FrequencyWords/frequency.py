from collections import Counter
import pandas as pd
import nltk
import re
import getMethods

hashtags = getMethods.getHashtags()

tweets= getMethods.getTweets()

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