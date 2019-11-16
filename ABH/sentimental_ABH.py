import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


analyser = SentimentIntensityAnalyzer()

tweets  = pd.read_csv('ABH/tweets_ABH.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])

tweets = tweets.drop_duplicates(subset='text', keep='first')

summary = {"positive":0,"neutral":0,"negative":0}

tweets_text = tweets["text"]

for x in tweets_text: 
    ss = analyser.polarity_scores(x)
    if ss["compound"] == 0.0: 
        summary["neutral"] +=1
    elif ss["compound"] > 0.0:
        summary["positive"] +=1
    else:
        summary["negative"] +=1

print(summary)


labels = 'Positive', 'Neutral', 'Negative'
sizes = [summary["positive"],summary["neutral"],summary["negative"]]
colors = ['yellowgreen','gold','lightcoral']
explode = (0.1, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()