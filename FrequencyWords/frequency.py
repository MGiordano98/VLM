from collections import Counter
import pandas as pd
import nltk
import re

tweets_nutella_biscuits  = pd.read_csv('CSV/nutella_biscuits.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
tweets_ABH  = pd.read_csv('CSV/ABH.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])

tweets_nutella_biscuits = tweets_nutella_biscuits.drop_duplicates(subset='text', keep='first')
tweets_ABH = tweets_ABH.drop_duplicates(subset='text', keep='first')

stopwords_it = nltk.corpus.stopwords.words('italian')
stopwords_en = nltk.corpus.stopwords.words('english')
stopwords = stopwords_it + stopwords_en
RE_stopwords = r'\b(?:{})\b'.format('|'.join(stopwords))


words_nutella_biscuits =[]
for t in tweets_nutella_biscuits["text"]:
    for i in t.split():
        if i.startswith('#'):
            words_nutella_biscuits.append(i)
  
words_ABH =[]
for t in tweets_ABH["text"]:
    for i in t.split():
        if i.startswith('#'):
            words_ABH.append(i)
  


# generate DF out of Counter
rslt_nutella_biscuits = pd.DataFrame(Counter(words_nutella_biscuits).most_common(10),columns=['Word', 'Frequency']).set_index('Word')

rslt_ABH = pd.DataFrame(Counter(words_ABH).most_common(10),columns=['Word', 'Frequency']).set_index('Word')

rslt_nutella_biscuits.head(5)