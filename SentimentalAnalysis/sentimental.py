import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


analyser = SentimentIntensityAnalyzer()

tweet_nutella_biscuits  = pd.read_csv('CSV/nutella_biscuits.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
tweet_ABH  = pd.read_csv('CSV/ABH.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])

tweet_nutella_biscuits = tweet_nutella_biscuits.drop_duplicates(subset='text', keep='first')
tweet_ABH = tweet_ABH.drop_duplicates(subset='text', keep='first')

summary_nutella_biscuits = {"positive":0,"neutral":0,"negative":0}
summary_ABH = {"positive":0,"neutral":0,"negative":0}

tweets_nutella_biscuits = tweet_nutella_biscuits["text"]
tweets_ABH = tweet_ABH["text"]

for x in tweets_nutella_biscuits: 
    ss = analyser.polarity_scores(x)
    if ss["compound"] == 0.0: 
        summary_nutella_biscuits["neutral"] +=1
    elif ss["compound"] > 0.0:
        summary_nutella_biscuits["positive"] +=1
    else:
        summary_nutella_biscuits["negative"] +=1
print(summary_nutella_biscuits)


for x in tweets_ABH: 
    ss = analyser.polarity_scores(x)
    if ss["compound"] == 0.0: 
        summary_ABH["neutral"] +=1
    elif ss["compound"] > 0.0:
        summary_ABH["positive"] +=1
    else:
        summary_ABH["negative"] +=1
print(summary_ABH)

labels = 'Positive', 'Neutral', 'Negative'
colors = ['yellowgreen','gold','lightcoral']


sizes_nutella_biscuits = [summary_nutella_biscuits["positive"],summary_nutella_biscuits["neutral"],summary_nutella_biscuits["negative"]]
sizes_ABH = [summary_ABH["positive"],summary_ABH["neutral"],summary_ABH["negative"]]
explode = (0.1, 0, 0)  # explode 1st slice
# Plot
plt.pie(sizes_nutella_biscuits, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()

plt.pie(sizes_ABH, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()