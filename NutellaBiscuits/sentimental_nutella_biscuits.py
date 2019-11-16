import re
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import string
import nltk
import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning)


train  = pd.read_csv('NutellaBiscuits/tweets_nutella_biscuits.csv',names=[ 'screen_name','text','date', 'favorite_count', 'retweet_count', 'location'])

train