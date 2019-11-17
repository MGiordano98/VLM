import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import nltk
from nltk.corpus import stopwords


tweet_nutella_biscuits  = pd.read_csv('CSV/nutella_biscuits.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])
tweet_ABH  = pd.read_csv('CSV/ABH.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])

tweet_nutella_biscuits = tweet_nutella_biscuits.drop_duplicates(subset='text', keep='first')
tweet_ABH = tweet_ABH.drop_duplicates(subset='text', keep='first')

stopwords_it = nltk.corpus.stopwords.words('italian')
stopwords_en = nltk.corpus.stopwords.words('english')
stopwords = stopwords_it + stopwords_en
RE_stopwords = r'\b(?:{})\b'.format('|'.join(stopwords))

words_nutella_biscuits = (tweet_nutella_biscuits["text"]
           .str.lower()
           .replace([r'\|',r'\&',r'\-',r'\.',r'\,',r'\'', RE_stopwords], [' ', '','','','','',''], regex=True)
           .str.cat(sep=' ')
           .replace('rt',' ')
           .replace('https',' ')           
           .replace('tco',' ')
           .split()
)

# join tweets to a single string
words = ' '.join(words_nutella_biscuits)

wordcloud = WordCloud(collocations=False,max_font_size=50, max_words=100, background_color="white").generate(words)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()






words_ABH = (tweet_ABH["text"]
           .str.lower()
           .replace([r'\|',r'\&',r'\-',r'\.',r'\,',r'\'', RE_stopwords], [' ', '','','','','',''], regex=True)
           .str.cat(sep=' ')
           .replace('rt',' ')
           .replace('https',' ')           
           .replace('tco',' ')
           .split()
)

# join tweets to a single string
words = ' '.join(words_ABH)

wordcloud = WordCloud(collocations=False,max_font_size=50, max_words=100, background_color="white").generate(words)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

