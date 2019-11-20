import json

# Credenziali di twitter
credentials = {}
credentials['CONSUMER_KEY'] = "M9aE9ycbpxFjHMkseJuSoLak7"
credentials['CONSUMER_SECRET'] = "UG0remo4I17nxUCeurEzdCCTShBaFAdffTzuf0xzY1goAbuimK"
credentials['ACCESS_TOKEN'] = "1192747749990653952-QSj54RyuMzxnmbOZE1Dddyri3pqIbm"
credentials['ACCESS_SECRET'] = "jVVxur00vqllJbWW29oQTrTbkHN6TYaScQx626Cppz4zy"

# Salvo le credenziali nel file
with open("CatchTweets/twitter_credentials.json", "w") as file:
    json.dump(credentials, file)