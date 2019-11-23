import pandas as pd
from collections import Counter
import csv
import json
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

until = "2019-11-23"

with open("CatchTweets/twitter_credentials.json", "r") as file:
    creds = json.load(file)
auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tweepy.API(auth,wait_on_rate_limit=True)

hashtags=[]
hashtags.append("#Puma") #November 22, 2019
#Halo Reach - December 3 (Xbox One)
#LiS 2: Episode 5 - December 3
#SaGa: Scarlet Grace - December 3
#Terminator: Resistance - December 5
#Assassins Creed: The Rebel Collection(Nintendo Switch) - December 6
#Ashen (PS4 and Switch) - December 9
#Narcos: Rise of the Cartels - December 10

csvFileWithDuplicate={}
csvWritersWithDuplicate={}
for i,val in enumerate(hashtags):
    csvFileWithDuplicate[val] = open('CSVwithDuplicate/'+val+'.csv', 'a', encoding="UTF-8")
    csvWritersWithDuplicate[val] = csv.writer(csvFileWithDuplicate[val])

for i,val in enumerate(hashtags):
    for tweet in tweepy.Cursor(api.search,
                            q=val,
                            until=until
                            ).items():
        csvWritersWithDuplicate[val].writerow([ tweet.user.screen_name, tweet.text,tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.user.location])

for i,val in enumerate(hashtags):
    df = pd.read_csv('CSVwithDuplicate/'+val+'.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
    df.drop_duplicates(subset=['screen_name','text'],inplace=True)
    df.to_csv('CSVwithoutDuplicate/'+val+'.csv', index=False)

tweets={}
for i,val in enumerate(hashtags):
    tweets[val] = pd.read_csv('CSVwithoutDuplicate/'+val+'.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])

words =  {}
wordsRT = {}
for i,val in enumerate(hashtags):
    x = []
    for t in tweets[val]["text"]:
        for i in t.split():
            if i.startswith('@') and i.endswith(':'):
                x.append(i)
    wow = pd.DataFrame(Counter(x).most_common(10),columns=['Word', 'Frequency']).set_index('Word')
    wordsRT[val] = wow 
csvFileCount = {}
csvWritersCount={}
for i,val in enumerate(hashtags):
    csvFileCount[val] = open('CountFollowers/'+val+'.csv', 'w', encoding="UTF-8")
    csvWritersCount[val] = csv.writer(csvFileCount[val])

for key,value in wordsRT.items():
    data = value.head()
    for i in data.index:
        i = i[:-1]
        if i!="@Concours__FR":
            user = api.get_user(i)
            csvWritersCount[key].writerow([user.screen_name, user.followers_count])