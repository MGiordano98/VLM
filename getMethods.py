import pandas as pd
from collections import Counter

def getHashtags():
    hashtags=[]
    hashtags.append("#NutellaBisciuts")
    hashtags.append("#ABH")
    hashtags.append('#HuaweiMateX')
    hashtags.append('#MiNote10')
    hashtags.append('#realme5pro')
    hashtags.append('#MotoG8Plus')
    return hashtags


def getTweets():
    tweets={}
    tweets["#NutellaBisciuts"] = pd.read_csv('CSV/nutella_biscuits.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
    tweets["#ABH"]  = pd.read_csv('CSV/ABH.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
    tweets["#HuaweiMateX"]  = pd.read_csv('CSV/HuaweiMateX.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
    tweets["#MiNote10"]  = pd.read_csv('CSV/MiNote10.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
    tweets["#realme5pro"]  = pd.read_csv('CSV/realme5pro.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
    tweets["#MotoG8Plus"]  = pd.read_csv('CSV/MotoG8Plus.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
    return tweets


def getRslt(x):
    return pd.DataFrame(Counter(x).most_common(10),columns=['Word', 'Frequency']).set_index('Word')
