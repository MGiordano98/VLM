from translate import Translator
import getMethods

hashtags = getMethods.getHashtags()
tweets = getMethods.getTweets()
translator= Translator(to_lang="en")

""" 
for t in tweets["#StarWarsJediFallenOrder"]["text"]:
    translation = translator.translate(t)
    print(translation)

 """

import tweepy
import csv
import pandas as pd
import unicodedata
import json
import getMethods
import time

# Load credentials from json file
with open("CatchTweets/twitter_credentials.json", "r") as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tweepy.API(auth,wait_on_rate_limit=True)

user = api.get_user('JeffreeStar')
print(user.screen_name)
print(user.followers_count)