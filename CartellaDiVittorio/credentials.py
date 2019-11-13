import json

consumer_key= "DvIJROlZmX32RctFrpQSRlHYj"
consumer_secret= "NG2rnPBQ2N26Z6PWfCNz5tUkthotDcjokb6T1CZTI5RqwmrQA1"
access_token= "1192747749990653952-CxqEA7iUvRx1N468HlZWxGUW1rkCSD"
access_token_secret= "5ndTXJx4hRfrMO4QrqN95YCIvAsXyi3SiAdEPkZmeO3g2"

credentials = {}
credentials['CONSUMER_KEY'] = consumer_key
credentials['CONSUMER_SECRET'] = consumer_secret
credentials['ACCESS_TOKEN'] = access_token
credentials['ACCESS_SECRET'] = access_token_secret

# Save the credentials object to file
with open("CartellaDiVittorio/twitter_credentials.json", "w") as file:
    json.dump(credentials, file)