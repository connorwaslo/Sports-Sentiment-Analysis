import nltk
import random
import pickle
import csv
import re

from sklearn.linear_model import LogisticRegression

from nltk.tokenize import word_tokenize

pos_tweets = []
with open('training_data/positive_tweets.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        tweet = row[0]
        pos_tweets.append(re.sub('&.+?;', '', tweet))

neg_tweets = []
with open('training_data/negative_tweets.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        tweet = row[0]
        neg_tweets.append(re.sub('&.+?;', '', tweet))
