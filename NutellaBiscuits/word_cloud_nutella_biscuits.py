import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import nltk
from nltk.corpus import stopwords


tweets  = pd.read_csv('NutellaBiscuits/tweets_nutella_biscuits.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])

tweets = tweets.drop_duplicates(subset='text', keep='first')

stopwords_it = nltk.corpus.stopwords.words('italian')
stopwords_en = nltk.corpus.stopwords.words('english')
stopwords = stopwords_it + stopwords_en

RE_stopwords = r'\b(?:{})\b'.format('|'.join(stopwords))
wordss = (tweets["text"]
           .str.lower()
           .replace([r'\|',r'\&',r'\-',r'\.',r'\,',r'\'', RE_stopwords], [' ', '','','','','',''], regex=True)
           .str.cat(sep=' ')
           .replace('rt',' ')
           .replace('https',' ')
           .split()
)

# join tweets to a single string
words = ' '.join(wordss)

wordcloud = WordCloud(collocations=False,max_font_size=50, max_words=100, background_color="white").generate(words)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()