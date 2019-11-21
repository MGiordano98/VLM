import pandas as pd
from collections import Counter
import csv
import json
import tweepy

# Credenziali di twitter
credentials = {}
credentials['CONSUMER_KEY'] = "M9aE9ycbpxFjHMkseJuSoLak7"
credentials['CONSUMER_SECRET'] = "UG0remo4I17nxUCeurEzdCCTShBaFAdffTzuf0xzY1goAbuimK"
credentials['ACCESS_TOKEN'] = "1192747749990653952-QSj54RyuMzxnmbOZE1Dddyri3pqIbm"
credentials['ACCESS_SECRET'] = "jVVxur00vqllJbWW29oQTrTbkHN6TYaScQx626Cppz4zy"

hashtags=[]
hashtags.append("#NutellaBiscuits")
hashtags.append("#ABH") 
hashtags.append('#HuaweiMateX')
hashtags.append('#MiNote10')
hashtags.append('#realme5pro')
hashtags.append('#MotoG8Plus')
hashtags.append('#StarWarsJediFallenOrder')
hashtags.append('#DeathStrading')
hashtags.append('#FootballManager2020')
hashtags.append('#DragonBallZKakarot')
hashtags.append('#OPPOReno2')
hashtags.append('#RedmiNote8T')
#hashtags.append('#PokemonSwordShield')

csvFileWithDuplicate={}
csvWritersWithDuplicate={}

tweets={}
summary={}
texts={}
sizes={}
words={}

csvFileCount = {}
csvWritersCount={}


def saveCredentials():
    with open("CatchTweets/twitter_credentials.json", "w") as file:
        json.dump(credentials, file)

def dropDuplicates():
    for i,val in enumerate(hashtags):
        df = pd.read_csv('CSVwithDuplicate/'+val+'.csv')
        df.drop_duplicates(inplace=True)
        df.to_csv('CSVwithoutDuplicate/'+val+'.csv', index=False)

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

def getCsvFileWithDuplicate():
    for i,val in enumerate(hashtags):
        csvFileWithDuplicate[val] = open('CSVwithDuplicate/'+val+'.csv', 'a', encoding="UTF-8")
    return csvFileWithDuplicate

def getWritersWithDuplicate():
    for i,val in enumerate(hashtags):
        csvWritersWithDuplicate[val] = csv.writer(csvFileWithDuplicate[val])
    return csvWritersWithDuplicate

def getCsvFileCount():
    for i,val in enumerate(hashtags):
        csvFileCount[val] = open('CountFollowers/'+val+'.csv', 'w', encoding="UTF-8")
    return csvFileCount

def getWritersCount():
    for i,val in enumerate(hashtags):
        csvWritersCount[val] = csv.writer(csvFileCount[val])
    return csvWritersCount

def getTweets():
    for i,val in enumerate(hashtags):
        tweets[val] = pd.read_csv('CSVwithoutDuplicate/'+val+'.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
    return tweets

def getInfluencer():
    x = {}
    for i,val in enumerate(hashtags):
        x[val] = pd.read_csv('CountFollowers/'+val+'.csv',names=[ 'screen_name', 'followers'])
    return x


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