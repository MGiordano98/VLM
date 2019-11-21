from twython import Twython
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hashtags=["#ABH", "#HuaweiMateX", "#MiNote10", "#MotoG8Plus", "#NutellaBiscuits", "#realme5pro", "#OPPOReno2", "#StarWarsJediFallenOrder", "#RedmiNote8T", "#FootballManager2020", "#DragonBallZKakarot", "#DeathStrading"]

for hashtag in hashtags:
    df  = pd.read_csv('CSVwithoutDuplicate/'+hashtag+'.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
    df = df.drop_duplicates(subset='text', keep='first')
    df.sort_values('date', inplace=True)

    count={}

    for i in range(0, len(df)):
        date=df.iloc[i].date.split()[0]
        if date in count:
            count[date]=count[date] + 1
        else:
            count[date]=0

    keys=[]
    for key in count.keys():
        keys.append(key.split("-")[2])

    plt.plot(keys, count.values(), label=hashtag)
    plt.xlabel('date')
    plt.ylabel('numero tweets')
    plt.legend()
    plt.show()