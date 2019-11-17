import json

# Credenziali di twitter
credentials = {}
credentials['CONSUMER_KEY'] = "DvIJROlZmX32RctFrpQSRlHYj"
credentials['CONSUMER_SECRET'] = "NG2rnPBQ2N26Z6PWfCNz5tUkthotDcjokb6T1CZTI5RqwmrQA1"
credentials['ACCESS_TOKEN'] = "1192747749990653952-CxqEA7iUvRx1N468HlZWxGUW1rkCSD"
credentials['ACCESS_SECRET'] = "5ndTXJx4hRfrMO4QrqN95YCIvAsXyi3SiAdEPkZmeO3g2"

# Salvo le credenziali nel file
with open("CatchTweets/twitter_credentials.json", "w") as file:
    json.dump(credentials, file)