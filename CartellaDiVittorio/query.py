from twython import Twython
import json
import pandas as pd


# Load credentials from json file
with open("CartellaDiVittorio/twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create our query
search_words = "#ABH"
date_since = "2019-11-13"
query = {'q': search_words,
        'result_type': 'recent',
        'count': 10,
        'lang': 'en',      
        'since':date_since
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
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df



