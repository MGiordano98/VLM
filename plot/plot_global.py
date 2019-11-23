from twython import Twython
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import getMethods

hashtags= getMethods.getHashtags()

for hashtag in hashtags:
    df  = pd.read_csv('CSVwithoutDuplicate/'+hashtag+'.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
    df.sort_values('date', inplace=True)
    df = df.drop(columns=[ 'screen_name','text', 'favorite_count', 'retweet_count', 'location'])

    keys=[]
    for key in df["date"]:
        if 'date' not in key:
            data = key.split("-")
            anno = data[0]
            mese = data[1]
            giorno = data[2].split(" ")
            keys.append(anno+"-"+mese+"-"+giorno[0])

    tutto = Counter(keys)
    lists = sorted(tutto.items())
    print(hashtag)
    print(lists)
    x, y = zip(*lists)
    plt.plot(x, y, color=np.random.rand(3,), label=hashtag)
    plt.xticks(rotation=90)
    plt.xlabel('date')
    plt.ylabel('# tweets')
    plt.title(hashtag)
    plt.show()