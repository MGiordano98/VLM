import tweepy
import csv
import pandas as pd
import unicodedata
import json
import getMethods
import time

tweets = getMethods.getTweets()
influencer = getMethods.getInfluencer()

tweets["#ABH"].loc[(tweets["#ABH"]['screen_name'] == 'ABHcosmetics')]

#tweets["#ABH"].loc[(tweets["#ABH"]['screen_name'] == 'ABHcosmetics') & tweets["#ABH"]['date'].str.contains("2019-11-17")]