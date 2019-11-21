import pandas as pd
from collections import Counter
import csv
import json
import tweepy


hashtags=[]
hashtags.append("#NutellaBiscuits")
hashtags.append("#ABH") 
hashtags.append('#HuaweiMateX')
hashtags.append('#MiNote10')
hashtags.append('#realme5pro')
hashtags.append('#MotoG8Plus')

hashtags.append('#PokemonSwordShield')

hashtags.append('#StarWarsJediFallenOrder')
hashtags.append('#DeathStrading')
hashtags.append('#FootballManager2020')
hashtags.append('#DragonBallZKakarot')
hashtags.append('#OPPOReno2')
hashtags.append('#RedmiNote8T')


csvs={}
csvWriters={}
tweets={}
summary={}
texts={}
sizes={}
words={}
csvc = {}
csvWritersC={}

def getApi():
    # Load credentials from json file
    with open("CatchTweets/twitter_credentials.json", "r") as file:
        creds = json.load(file)
    auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
    auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
    api = tweepy.API(auth,wait_on_rate_limit=True)
    return api


def getHashtags():
    return hashtags

def getCsvFile():
    for i,val in enumerate(hashtags):
        csvs[val] = open('CSVwithDuplicate/'+val+'.csv', 'a', encoding="UTF-8")
    return csvs

def getCsvCount():
    for i,val in enumerate(hashtags):
        csvc[val] = open('CountFollowers/'+val+'.csv', 'a', encoding="UTF-8")
    return csvs

def getWriters():
    for i,val in enumerate(hashtags):
        csvWriters[val] = csv.writer(csvs[val])
    return csvWriters

def getWritersCount():
    for i,val in enumerate(hashtags):
        csvWritersC[val] = csv.writer(csvc[val])
    return csvWritersC



def getTweets():
    for i,val in enumerate(hashtags):
        tweets[val] = pd.read_csv('CSVwithoutDuplicate/'+val+'.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
    return tweets


def getRslt(x):
    return pd.DataFrame(Counter(x).most_common(10),columns=['Word', 'Frequency']).set_index('Word')

def getSummary():
    for i,val in enumerate(hashtags):
        summary[val] = {"positive":0,"neutral":0,"negative":0}
    return summary

def getSizes(summary):
    for i,val in enumerate(hashtags):
        sizes[val] = [summary[val]["positive"],summary[val]["neutral"],summary[val]["negative"]]
    return sizes


def getWords(tweets,RE_stopwords):
    for i,val in enumerate(hashtags):
        words[val]= (tweets[val]["text"]
           .str.lower()
           .replace([r'\|',r'\&',r'\-',r'\.',r'\,',r'\'', RE_stopwords], [' ', '','','','','',''], regex=True)
           .str.cat(sep=' ')
           .replace('rt',' ')
           .replace('https',' ')           
           .replace('tco',' ')
           .split()
            )
    return words


def checkDates():
    for i,val in enumerate(hashtags):
        print(val)
        PD = pd.read_csv('CSVwithoutDuplicate/'+val+'.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
        PD.sort_values(by='date', inplace=True, ascending=False)
        print(PD["date"])
        print("----------------")