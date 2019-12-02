import pandas as pd
from collections import Counter
import csv
import json
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from googletrans import Translator

# Credenziali di twitter
credentials = {}
credentials['CONSUMER_KEY'] = "M9aE9ycbpxFjHMkseJuSoLak7"
credentials['CONSUMER_SECRET'] = "UG0remo4I17nxUCeurEzdCCTShBaFAdffTzuf0xzY1goAbuimK"
credentials['ACCESS_TOKEN'] = "1192747749990653952-QSj54RyuMzxnmbOZE1Dddyri3pqIbm"
credentials['ACCESS_SECRET'] = "jVVxur00vqllJbWW29oQTrTbkHN6TYaScQx626Cppz4zy"

hashtags=[]
hashtags.append("#NutellaBiscuits")
hashtags.append("#ABH") 
hashtags.append('#HuaweiMateX') #15 novembre 2019
hashtags.append('#MiNote10') #25 dicembre 2019
hashtags.append('#realme5pro') #20th August 2019
hashtags.append('#MotoG8Plus') #October 25 2019
hashtags.append('#StarWarsJediFallenOrder') #November 15, 2019
hashtags.append('#DeathStrading') #November 8, 2019
hashtags.append('#FootballManager2020') #18 November 2019
hashtags.append('#DragonBallZKakarot') #16 gennaio 2019
hashtags.append('#OPPOReno2') #September 20 2019
hashtags.append('#RedmiNote8T') #6th November 2019
#hashtags.append('#PokemonSwordShield')
hashtags.append('#ShenmueIII') #19 novembre 2019
hashtags.append("#SGWContracts") #November 22, 2019

hashtags.append('#Jordan') #November 23, 2019
hashtags.append("#adidas") #November 23, 2019
hashtags.append("#AIRFORCE1") #November 22, 2019
hashtags.append("#Puma") #November 22, 2019
hashtags.append('#nike') #November 22-23, 2019

hashtags.append('#HaloReach') #Halo Reach - December 3 (Xbox One)
hashtags.append("#LifeisStrange2") #LiS 2: Episode 5 - December 3
hashtags.append("#TerminatorResistance") #Terminator: Resistance - December 5
hashtags.append("#Ashen") #Ashen (PS4 and Switch) - December 9
hashtags.append("#Narcos") #Narcos: Rise of the Cartels - December 10

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
        print(val)
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

"""     tweets={}
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
 """

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

    tweets[hashtag].sort_values('date', inplace=True)

    giornocorrente = date+" 23:59:59"
    anno,mese,giorno = date.split("-")
    giornoprima = anno+"-"+mese+"-"+str(int(giorno)-1)+" 00:00:01"
    giornodopo = anno+"-"+mese+"-"+str(int(giorno)+1)+" 23:59:59"

    mask = (tweets[hashtag]['date'] > giornoprima) & (tweets[hashtag]['date'] <= giornocorrente)
    x = tweets[hashtag].loc[mask]
    influenzers=[]
    for t in x["text"]:
        for i in t.split():
            if i.startswith('@') and i.endswith(':'):
                influenzers.append(i)
    influenzer = pd.DataFrame(Counter(influenzers).most_common(10),columns=['Word', 'Frequency']).set_index('Word')
    influenzerTR = influenzer['Frequency'][0]
    influenzer = influenzer.index
    influenzer = influenzer[0]
    influenzer = influenzer[:-1]
    influenzer = influenzer[1:]
    print("Nome dell'influenzer, del giorno:"+date+", e' "+influenzer+"\n")
    print("Su "+str(len(x))+" tweets lui/lei è stata retweettata ben "+str(influenzerTR))

    tweet = tweets[hashtag].loc[(tweets[hashtag]['screen_name'] == influenzer)] 
    tweet = tweet.loc[(tweet['date'] < giornocorrente)]
    tweet = tweet.loc[(tweet['date'] > giornoprima)]

    print("Testo = "+tweet["text"])
    print("Data = "+tweet["date"])
    translator = Translator()
    #translation = translator.translate(str(tweet["text"]), dest='it')
    #print(translation.text)

    print("\n")
    with open("CatchTweets/twitter_credentials.json", "r") as file:
        creds = json.load(file)
    auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
    auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
    api = tweepy.API(auth,wait_on_rate_limit=True)
    user = api.get_user("@"+influenzer)
    print("I followers dell'influenzer sono = "+str(user.followers_count))

    prima = tweets[hashtag].loc[tweets[hashtag]['date'] <= date+" 00:00:00"]
    durante = tweets[hashtag].loc[tweets[hashtag]['date'] <= date+" 23:59:59"]
    dopo = tweets[hashtag][tweets[hashtag]['date'] <= giornodopo]
    getSentimental(hashtag,tweet,influenzer)
    getSentimental(hashtag,prima)
    getSentimental(hashtag,durante)
    getSentimental(hashtag,dopo)













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
    
    tweets.sort_values(by='date', inplace=True, ascending=True)
    
    if colpevole=="":
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
        plt.title(hashtag + "\n  "  + "\nColpevole : "+colpevole)
    plt.legend(sizes[hashtag])
    plt.show()