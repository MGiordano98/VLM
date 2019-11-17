from collections import Counter
import pandas as pd
import nltk

tweets  = pd.read_csv('NutellaBiscuits/tweets_nutella_biscuits.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])

tweets = tweets.drop_duplicates(subset='text', keep='first')

stopwords_it = nltk.corpus.stopwords.words('italian')
stopwords_en = nltk.corpus.stopwords.words('english')
stopwords = stopwords_it + stopwords_en

RE_stopwords = r'\b(?:{})\b'.format('|'.join(stopwords))
words = (tweets["text"]
           .str.lower()
           .replace([r'\|',r'\&',r'\-',r'\.',r'\,',r'\'', RE_stopwords], [' ', '','','','','',''], regex=True)
           .str.cat(sep=' ')
           .replace('rt',' ')
           .split()
)

# generate DF out of Counter
rslt = pd.DataFrame(Counter(words).most_common(10),
                    columns=['Word', 'Frequency']).set_index('Word')
rslt