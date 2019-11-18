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
csvWriterNutellaBiscuits = csv.writer(csvNutellaBiscuits)
csvWriterABH = csv.writer(csvABH)

csvWriterHuaweiMateX = csv.writer(csvHuaweiMateX)
csvWriterMiNote10 = csv.writer(csvMiNote10)
csvWriterrealme5pro = csv.writer(csvrealme5pro)
csvWriterMotoG8Plus = csv.writer(csvMotoG8Plus)


since = "2019-11-17"
until = "2019-11-18"
#Se voglio prendere i tweet di un giorno, esempio del 2019-11-16, devo mettere since="2019-11-16" e until del giorno dopo quindi="2019-11-17"

""" hashtag="#NutellaBiscuits"
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
 """

""" hashtag="#HuaweiMateX"
for tweet in tweepy.Cursor(api.search,
                            q=hashtag,
                            until=until).items():
    csvWriterHuaweiMateX.writerow([ tweet.user.screen_name, tweet.text,tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.user.location])

hashtag="#MiNote10"
for tweet in tweepy.Cursor(api.search,
                            q=hashtag,
                            until=until).items():
    csvWriterMiNote10.writerow([ tweet.user.screen_name, tweet.text,tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.user.location])
 """
 
hashtag="#realme5pro"
for tweet in tweepy.Cursor(api.search,
                            q=hashtag,
                            until=until).items():
    csvWriterrealme5pro.writerow([ tweet.user.screen_name, tweet.text,tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.user.location])

hashtag="#MotoG8Plus"
for tweet in tweepy.Cursor(api.search,
                            q=hashtag,
                            until=until).items():
    csvWriterMotoG8Plus.writerow([ tweet.user.screen_name, tweet.text,tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.user.location])



#Nutella = pd.read_csv('CSV/nutella_biscuits.csv', names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
#Nutella.sort_values(by='date', inplace=True, ascending=False)
#Nutella