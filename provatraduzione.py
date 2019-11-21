import tweepy
import csv
import pandas as pd
import unicodedata
import json
import getMethods
import time

tweets = getMethods.getTweets()
influencer = getMethods.getInfluencer()


x = tweets["#realme5pro"].loc[(tweets["#realme5pro"]['date'].str.contains("2019-11-19"))]

asd=[]
for t in x["text"]:
    for i in t.split():
        if i.startswith('@') and i.endswith(':'):
            asd.append(i)
colpevole = getMethods.getRslt(asd)
colpevole = colpevole.index
colpevole = colpevole[0]
colpevole = colpevole[:-1]
colpevole = colpevole[1:]
print(colpevole)

print("\n")
yyy = tweets["#realme5pro"].loc[(tweets["#realme5pro"]['screen_name'] == colpevole)] #& tweets["#FootballManager2020"]['date'].str.contains("2019-11-17")]
print(yyy["text"])

print("\n")
influenzer = influencer["#realme5pro"].loc[(influencer["#realme5pro"]['screen_name'] == colpevole)] #& tweets["#FootballManager2020"]['date'].str.contains("2019-11-17")]
influenzer

