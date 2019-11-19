import pandas as pd
import getMethods


hashtags = getMethods.getHashtags()

for i,val in enumerate(hashtags):
        df = pd.read_csv('CSV/'+val+'.csv')
        df.drop_duplicates(inplace=True)
        df.to_csv('CSV/'+val+'.csv', index=False)

""" hashtags = getMethods.getHashtags()

tweets = getMethods.getTweets()
tweets1={}

print(len(tweets["#ABH"]["text"]))

for i,val in enumerate(hashtags):
        tweets1[val] = pd.read_csv('CSV/'+'#ABH1'+'.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
    
print(len(tweets1["#ABH"]["text"])) """