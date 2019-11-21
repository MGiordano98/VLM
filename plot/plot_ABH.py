from twython import Twython
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_counter():
    df  = pd.read_csv('CSV/#ABH.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
    df = df.drop_duplicates(subset='text', keep='first')
    df.sort_values('date', inplace=True)

    count={}

    for i in range(0, len(df)):
        date=df.iloc[i].date.split()[0]
        if date in count:
            count[date]=count[date] + 1
        else:
            count[date]=0

    return count

count=calculate_counter()
plt.plot(count.keys(), count.values(), label="ABH")
plt.xlabel('date')
plt.ylabel('numero tweets')
plt.legend()
plt.show()