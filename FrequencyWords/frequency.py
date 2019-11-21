from collections import Counter
import pandas as pd
import nltk
import re
import getMethods

hashtags = getMethods.getHashtags()

tweets = getMethods.getTweets()



words =  {}
wordsRT = {}
dizionario = {}
for i,val in enumerate(hashtags):
    x = []
    for t in tweets[val]["text"]:
        for i in t.split():
            if i.startswith('@') and i.endswith(':'):
                x.append(i)
    wow = getMethods.getRslt(x)
    wordsRT[val] = wow


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
