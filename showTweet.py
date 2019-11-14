import tweepy
import csv
import pandas as pd


df = pd.read_csv('ua.csv', names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df