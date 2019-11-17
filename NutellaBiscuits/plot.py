import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

tweets_nutella_biscuits = "NutellaBiscuits/tweets_nutella_biscuits.csv"


df = pd.read_csv(tweets_nutella_biscuits, names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
df.sort_values(by='date', inplace=True, ascending=True)

count={}
len(df.index)
for i in range(0, len(df.index)):
    date= df.iloc[i].date.split()[0]
    if date in count:
        count[date]= count[date]+1
    else:
        count[date]=0

print(count)
plt.figure()
plt.plot(count.keys(),count.values(),label='nutella biscuits')
plt.xlabel('data')
plt.ylabel('numero tweets')
plt.legend()
plt.show()