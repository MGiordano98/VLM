# my twitter app credentials
consumer_key = "DvIJROlZmX32RctFrpQSRlHYj"
consumer_secret = "NG2rnPBQ2N26Z6PWfCNz5tUkthotDcjokb6T1CZTI5RqwmrQA1"

access_token = "1192747749990653952-CxqEA7iUvRx1N468HlZWxGUW1rkCSD"
access_token_secret = "5ndTXJx4hRfrMO4QrqN95YCIvAsXyi3SiAdEPkZmeO3g2"

# Import the Twython class
from twython import Twython
import json

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds[consumer_key], creds[consumer_secret])

# Create our query
query = {'q': 'learn python',
        'result_type': 'popular',
        'count': 10,
        'lang': 'en',
        }