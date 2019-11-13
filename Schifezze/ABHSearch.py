import os
import tweepy as tw
import pandas as pd

consumer_key= "DvIJROlZmX32RctFrpQSRlHYj"
consumer_secret= "NG2rnPBQ2N26Z6PWfCNz5tUkthotDcjokb6T1CZTI5RqwmrQA1"
access_token= "1192747749990653952-CxqEA7iUvRx1N468HlZWxGUW1rkCSD"
access_token_secret= "5ndTXJx4hRfrMO4QrqN95YCIvAsXyi3SiAdEPkZmeO3g2"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Post a tweet from Python
# api.update_status("Look, I'm tweeting from #Python in my #earthanalytics class! @EarthLabCU")
# Your tweet has been posted!


search_words = "#ABH"
date_since = "2019-11-13"

# Collect tweets
#You can restrict the number of tweets returned by specifying a number in the .items()
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since,
              result_type="recent").items(20)


users = []
for tweet in tweets:
    tweeter = [tweet.user.screen_name, tweet.user.location, tweet.favorite_count, tweet.created_at, tweet.text]
    users.append(tweeter)

tweet_text = pd.DataFrame(data=users, 
                    columns=['user', "location","favorite_count","created_at","text"])
tweet_text

tweet_text.sort_values(by='favorite_count', inplace=True, ascending=False)
tweet_text.head(5)





