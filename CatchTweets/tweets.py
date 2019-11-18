import tweepy
import csv
import pandas as pd
import unicodedata
import json

# Load credentials from json file
with open("CatchTweets/twitter_credentials.json", "r") as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvNutellaBiscuits = open('CSV/nutella_biscuits.csv', 'a', encoding="UTF-8")
csvABH = open('CSV/ABH.csv', 'a', encoding="UTF-8")
csvHuaweiMateX = open('CSV/HuaweiMateX.csv', 'a', encoding="UTF-8")
csvMiNote10 = open('CSV/MiNote10.csv', 'a', encoding="UTF-8")
csvrealme5pro = open('CSV/realme5pro.csv', 'a', encoding="UTF-8")
csvMotoG8Plus = open('CSV/MotoG8Plus.csv', 'a', encoding="UTF-8")


#Use csv Writer
csvWriters={}
csvWriters['#NutellaBisciuts'] = csv.writer(csvNutellaBiscuits)
csvWriters['#ABH'] = csv.writer(csvABH)
csvWriters['#HuaweiMateX'] = csv.writer(csvHuaweiMateX)
csvWriters['#MiNote10'] = csv.writer(csvMiNote10)
csvWriters['#realme5pro'] = csv.writer(csvrealme5pro)
csvWriters['#MotoG8Plus'] = csv.writer(csvMotoG8Plus)

hashtags=[]
hashtags.append("#NutellaBisciuts")
hashtags.append("#ABH")
hashtags.append('#HuaweiMateX')
hashtags.append('#MiNote10')
hashtags.append('#realme5pro')
hashtags.append('#MotoG8Plus')
n = len(hashtags)
since = "2019-11-17"
until = "2019-11-18"
#Se voglio prendere i tweet di un giorno, esempio del 2019-11-16, devo mettere since="2019-11-16" e until del giorno dopo quindi="2019-11-17"


for i,val in enumerate(hashtags):
    for tweet in tweepy.Cursor(api.search,
                            q=val,
                            since=since,
                            until=until).items():
        csvWriters[val].writerow([ tweet.user.screen_name, tweet.text,tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.user.location])




#Nutella = pd.read_csv('CSV/nutella_biscuits.csv', names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
#Nutella.sort_values(by='date', inplace=True, ascending=False)
#Nutella