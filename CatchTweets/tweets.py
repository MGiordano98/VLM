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

#Use csv Writer
csvWriterNutellaBiscuits = csv.writer(csvNutellaBiscuits)
csvWriterABH = csv.writer(csvABH)

since = "2019-11-16"
until = "2019-11-17"
#Se voglio prendere i tweet di un giorno, esempio del 2019-11-16, devo mettere since="2019-11-16" e until del giorno dopo quindi="2019-11-17"

hashtag="#NutellaBiscuits"
for tweet in tweepy.Cursor(api.search,
                            q=hashtag,
                            since=since,
                            until=until).items():
    csvWriterNutellaBiscuits.writerow([ tweet.user.screen_name, tweet.text,tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.user.location])

hashtag="#ABH"
for tweet in tweepy.Cursor(api.search,
                            q=hashtag,
                            since=since,
                            until=until).items():
    csvWriterABH.writerow([ tweet.user.screen_name, tweet.text,tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.user.location])





#Nutella = pd.read_csv('CSV/nutella_biscuits.csv', names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
#Nutella.sort_values(by='date', inplace=True, ascending=False)
#Nutella