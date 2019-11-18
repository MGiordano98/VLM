import tweepy
import csv
import pandas as pd
import unicodedata
import json
import getMethods

# Load credentials from json file
with open("CatchTweets/twitter_credentials.json", "r") as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tweepy.API(auth,wait_on_rate_limit=True)

#Ottengo tutti gli hashtag
hashtags= getMethods.getHashtags()

#Apro/Creo il file dove devo scrivere i dati
csvs = getMethods.getCsvFile()

#Use csv Writer
csvWriters = getMethods.getWriters()

since = "2019-11-17"
until = "2019-11-18"
#Se voglio prendere i tweet di un giorno, esempio del 2019-11-16, devo mettere since="2019-11-16" e until del giorno dopo quindi="2019-11-17"


for i,val in enumerate(hashtags):
    for tweet in tweepy.Cursor(api.search,
                            q=val#,
                            #since=since,
                            #until=until,
                            #lang="en"
                            ).items():
        csvWriters[val].writerow([ tweet.user.screen_name, tweet.text,tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.user.location])




#Nutella = pd.read_csv('CSV/nutella_biscuits.csv', names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
#Nutella.sort_values(by='date', inplace=True, ascending=False)
#Nutella