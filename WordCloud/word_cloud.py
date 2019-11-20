import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import nltk
from nltk.corpus import stopwords
import getMethods

hashtags = getMethods.getHashtags()

tweets = getMethods.getTweets()

stopwords_it = nltk.corpus.stopwords.words('italian')
stopwords_en = nltk.corpus.stopwords.words('english')
stopwords_fr = nltk.corpus.stopwords.words('french')
stopwords = stopwords_it + stopwords_en + stopwords_fr
RE_stopwords = r'\b(?:{})\b'.format('|'.join(stopwords))

words = getMethods.getWords(tweets,RE_stopwords)

for key,value in words.items():
    word = ' '.join(value)
    wordcloud = WordCloud(collocations=False,max_font_size=50, max_words=50, background_color="white").generate(word)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(key)
    plt.show()
# join tweets to a single string

