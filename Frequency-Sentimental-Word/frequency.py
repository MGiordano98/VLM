from collections import Counter
import pandas as pd
import nltk
import re
import getMethods
import csv
import tweepy
import json

hashtags = getMethods.getHashtags()

tweets = getMethods.getTweets()

words =  {}
wordsRT = {}
for i,val in enumerate(hashtags):
    x = []
    for t in tweets[val]["text"]:
        for i in t.split():
            if i.startswith('@') and i.endswith(':'):
                x.append(i)
    wow = getMethods.getRslt(x)
    wordsRT[val] = wow





api = getMethods.getApi()

csvc = getMethods.getCsvFileCount()
csvWriterC = getMethods.getWritersCount()



for key,value in wordsRT.items():
    data = value.head()
    for i in data.index:
        i = i[:-1]
        if i!="@Concours__FR":
            user = api.get_user(i)
            csvWriterC[key].writerow([user.screen_name, user.followers_count])