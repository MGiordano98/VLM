import tweepy
import csv
import pandas as pd
import unicodedata
import json

# Load credentials from json file
with open("CatchTweets/twitter_credentials2.json", "r") as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tweepy.API(auth,wait_on_rate_limit=True)

""" def get_followers(api, account_name):

        followers = []
        for page in tweepy.Cursor(api.followers_ids, screen_name=str(account_name)).pages():
            followers.extend(page)
        return followers 

followers= get_followers(api, "@Nutella_Italia")

print(followers) """

count={}
follower=[]
for user in tweepy.Cursor(api.followers, screen_name="Nutella_Italia").items():
    follower.append(user.screen_name)
    print(user)

print(len(follower))