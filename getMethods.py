import pandas as pd
from collections import Counter
import csv
import json
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Credenziali di twitter
credentials = {}
credentials['CONSUMER_KEY'] = "M9aE9ycbpxFjHMkseJuSoLak7"
credentials['CONSUMER_SECRET'] = "UG0remo4I17nxUCeurEzdCCTShBaFAdffTzuf0xzY1goAbuimK"
credentials['ACCESS_TOKEN'] = "1192747749990653952-QSj54RyuMzxnmbOZE1Dddyri3pqIbm"
credentials['ACCESS_SECRET'] = "jVVxur00vqllJbWW29oQTrTbkHN6TYaScQx626Cppz4zy"

hashtags=[]
hashtags.append("#NutellaBiscuits")
hashtags.append("#ABH") 
hashtags.append('#HuaweiMateX')
hashtags.append('#MiNote10')
hashtags.append('#realme5pro')
hashtags.append('#MotoG8Plus')
hashtags.append('#StarWarsJediFallenOrder')
hashtags.append('#DeathStrading')
hashtags.append('#FootballManager2020')
hashtags.append('#DragonBallZKakarot')
hashtags.append('#OPPOReno2')
hashtags.append('#RedmiNote8T')
#hashtags.append('#PokemonSwordShield')

analyser = SentimentIntensityAnalyzer()


summary={}
texts={}
sizes={}
words={}

def CatchTweet(since,until):
    with open("CatchTweets/twitter_credentials.json", "r") as file:
        creds = json.load(file)
    auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
    auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
    api = tweepy.API(auth,wait_on_rate_limit=True)

    hashtags= getHashtags()
    csvFileWithDuplicate={}
    csvWritersWithDuplicate={}
    for i,val in enumerate(hashtags):
        csvFileWithDuplicate[val] = open('CSVwithDuplicate/'+val+'.csv', 'a', encoding="UTF-8")
        csvWritersWithDuplicate[val] = csv.writer(csvFileWithDuplicate[val])

    for i,val in enumerate(hashtags):
        for tweet in tweepy.Cursor(api.search,
                                q=val,
                                since=since,
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


def saveCredentials():
    with open("CatchTweets/twitter_credentials.json", "w") as file:
        json.dump(credentials, file)

def getHashtags():
    return hashtags

def getTweets():
    tweets={}
    for i,val in enumerate(hashtags):
        tweets[val] = pd.read_csv('CSVwithoutDuplicate/'+val+'.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
    return tweets

def getInfluencer():
    influcer = {}
    for i,val in enumerate(hashtags):
        influcer[val] = pd.read_csv('CountFollowers/'+val+'.csv',names=[ 'screen_name', 'followers'])
    return influcer

def getSummary():
    for i,val in enumerate(hashtags):
        summary[val] = {"positive":0,"neutral":0,"negative":0}
    return summary

def getSizes(summary):
    for i,val in enumerate(hashtags):
        sizes[val] = [summary[val]["positive"],summary[val]["neutral"],summary[val]["negative"]]
    return sizes


def getWords(tweets,RE_stopwords):
    for i,val in enumerate(hashtags):
        words[val]= (tweets[val]["text"]
           .str.lower()
           .replace([r'\|',r'\&',r'\-',r'\.',r'\,',r'\'', RE_stopwords], [' ', '','','','','',''], regex=True)
           .str.cat(sep=' ')
           .replace('rt',' ')
           .replace('https',' ')           
           .replace('tco',' ')
           .split()
            )
    return words


def checkDates():
    for i,val in enumerate(hashtags):
        print(val)
        PD = pd.read_csv('CSVwithoutDuplicate/'+val+'.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
        PD.sort_values(by='date', inplace=True, ascending=False)
        print(PD["date"])
        print("----------------")














def TopInfluncerByDate(hashtag,date):     
    tweets = getTweets()
    influencer = getInfluencer()
    tweets[hashtag].sort_values('date', inplace=True)
    x = tweets[hashtag].loc[(tweets[hashtag]['date'].str.contains(date))]
    asd=[]
    for t in x["text"]:
        for i in t.split():
            if i.startswith('@') and i.endswith(':'):
                asd.append(i)
    colpevole = pd.DataFrame(Counter(asd).most_common(10),columns=['Word', 'Frequency']).set_index('Word')
    colpevole = colpevole.index
    colpevole = colpevole[0]
    colpevole = colpevole[:-1]
    colpevole = colpevole[1:]
    print(colpevole)
    print("\n")
    yyy = tweets[hashtag].loc[(tweets[hashtag]['screen_name'] == colpevole)] 
    print(yyy)
    print("\n")
    influenzer = influencer[hashtag].loc[(influencer[hashtag]['screen_name'] == colpevole)]
    print(influenzer)

    print(yyy.index[0])
    prima = tweets[hashtag].loc[:yyy.index[0]]
    dopo = tweets[hashtag].loc[yyy.index[0]:]

    getSentimental(hashtag,prima)
    nome = influenzer.iloc[0][0]
    followers = influenzer.iloc[0][1]
    getSentimental(hashtag,tweets[hashtag], str(nome)+" "+str(followers))













def getSentimental(hashtag,tweets,colpevole=""):
    dates = {}
    summary = getSummary()

    for text in tweets["text"]:
        ss = analyser.polarity_scores(text)
        if ss["compound"] == 0.0: 
            summary[hashtag]["neutral"] +=1
        elif ss["compound"] > 0.0:
            summary[hashtag]["positive"] +=1
        else:
            summary[hashtag]["negative"] +=1
    tweets.sort_index(by='date', inplace=True, ascending=True)
    df = tweets.reset_index(drop=True)
    dates[hashtag] = "Start ="+df["date"][0] + "   to ="+df["date"][len(df["date"])-2]

    labels = ['Positive', 'Neutral', 'Negative']
    colors = ['yellowgreen','gold','lightcoral']

    sizes = getSizes(summary)

    explode = (0.1, 0, 0)  # explode 1st slice
    # Plot
    plt.pie(sizes[hashtag], explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    if colpevole=="":
        plt.title(hashtag + "\n  " + dates[hashtag])
    else:
        plt.title(hashtag + "\n  " + dates[hashtag] + "\nColpevole : "+colpevole)
    plt.legend(sizes[hashtag])
    plt.show()