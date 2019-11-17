import tweepy
import csv
import pandas as pd

tweets_nutella_biscuits = "NutellaBiscuits/tweets_nutella_biscuits.csv"
tweets_ABH = "ABH/tweets_ABH.csv"


nutella_biscuits = pd.read_csv(tweets_nutella_biscuits, names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
nutella_biscuits.sort_values(by='date', inplace=True, ascending=False)
nutella_biscuits

ABH = pd.read_csv(tweets_ABH, names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
ABH.sort_values(by='date', inplace=True, ascending=False)
ABH

nutella_biscuits