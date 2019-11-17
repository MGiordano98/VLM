import tweepy
import csv
import pandas as pd
import unicodedata

####input your credentials here
consumer_key= "DvIJROlZmX32RctFrpQSRlHYj"
consumer_secret= "NG2rnPBQ2N26Z6PWfCNz5tUkthotDcjokb6T1CZTI5RqwmrQA1"
access_token= "1192747749990653952-CxqEA7iUvRx1N468HlZWxGUW1rkCSD"
access_token_secret= "5ndTXJx4hRfrMO4QrqN95YCIvAsXyi3SiAdEPkZmeO3g2"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('NutellaBiscuits/tweets_nutella_biscuits.csv', 'a', encoding="UTF-8")

#Use csv Writer
csvWriter = csv.writer(csvFile)

hashtag="#NutellaBiscuits"
since = "2019-11-16"
until = "2019-11-17"

#Se voglio prendere i tweet di un giorno, esempio del 2019-11-16, devo mettere since="2019-11-16" e until del giorno dopo quindi="2019-11-17"

for tweet in tweepy.Cursor(api.search,
                            q=hashtag,
                            since=since,
                            until=until).items():
    csvWriter.writerow([ tweet.user.screen_name, tweet.text,tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.user.location])
#Variables that contains the user credentials to access Twitter API 


