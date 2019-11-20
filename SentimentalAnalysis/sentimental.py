import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import getMethods

analyser = SentimentIntensityAnalyzer()

hashtags = getMethods.getHashtags()

tweets = getMethods.getTweets()

summary = getMethods.getSummary()

dates = {}

for key,value in tweets.items():
    for text in value["text"]:
        ss = analyser.polarity_scores(text)
        if ss["compound"] == 0.0: 
            summary[key]["neutral"] +=1
        elif ss["compound"] > 0.0:
            summary[key]["positive"] +=1
        else:
            summary[key]["negative"] +=1
    value.sort_index(by='date', inplace=True, ascending=True)
    df = value.reset_index(drop=True)
    dates[key] = "Start ="+df["date"][0] + "   to ="+df["date"][len(df["date"])-1]


labels = ['Positive', 'Neutral', 'Negative']
colors = ['yellowgreen','gold','lightcoral']

sizes = getMethods.getSizes(summary)

explode = (0.1, 0, 0)  # explode 1st slice
# Plot
for i,val in enumerate(hashtags):
    plt.pie(sizes[val], explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title(val + "  " + dates[val])
    plt.legend(sizes[val])
    plt.show()
