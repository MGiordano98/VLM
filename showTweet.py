import tweepy
import csv
import pandas as pd

tweets_nutella_biscuits = "NutellaBiscuits/tweets_nutella_biscuits.csv"


df = pd.read_csv(tweets_nutella_biscuits, names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
df.sort_values(by='date', inplace=True, ascending=False)
df