from twython import Twython
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load credentials from json file
with open("CatchTweets/twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create our query
search_words = '#nutella'
day= '8'
month= '11'
year= '2019'

plt.figure()

arr=[]
for i in range(0,7):
    
    day_since = str(int(day) + i)
    day_until = str(int(day) + i+1)
    date_since = year + "-" + month + "-" + day_since
    date_until = year + "-" + month + "-" + day_until
    print(date_since)
    print(date_until)

    query = {'q': search_words,
            'result_type': 'recent',
            'count': 100,
            'lang': 'en',      
            'since':date_since,
            'until':date_until
            }



    # Search tweets
    dict_ = {'user': [], 'date': [], 'location': [], 'text': [], 'favorite_count': [], 'retweet_count': []}

    for status in python_tweets.search(**query)['statuses']:
        dict_['user'].append(status['user']['screen_name'])
        dict_['date'].append(status['created_at'])
        dict_['location'].append(status['user']['location'])
        dict_['text'].append(status['text'])
        dict_['favorite_count'].append(status['favorite_count'])
        dict_['retweet_count'].append(status['retweet_count'])

    # Structure data in a pandas DataFrame for easier manipulation
    df = pd.DataFrame(dict_)
    df
    arr.append(len(df))

plt.plot(arr, label=search_words)
plt.title('')
plt.xlabel('giorno')
plt.ylabel('numero treets')
plt.legend()
plt.show()

""" 
a = pd.DataFrame(np.random.rand(4,5), columns = list('abcde'))
a_asarray = a.values
print(a_asarray)
plt.plot(a_asarray)
 """
