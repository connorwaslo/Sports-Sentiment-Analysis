import sentiment_analyzer as s
import tweet_preprocessing as tp
import pickle
import csv
import re

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

pos_tweets = tp.ProcessTweets('testing_data/nba_tweets.csv', 'testing_data/processed_nba_tweets.csv').get_tweets()

# pos_tweets = []
# with open('testing_data/nba_tweets.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         tweet = row[0]
#         pos_tweets.append(re.sub('&.+?;', '', tweet)) # Delete words like &quot;

# Test accuracy of Vader sentiment analysis
documents_f = open('pickles/documents.pickle', 'rb')
documents = pickle.load(documents_f)
documents_f.close()

# Use same testing set as other classifiers
testing_set = pos_tweets #  documents[:1000]

# print(testing_set[0][0], testing_set[0][1])
# print(s.sentiment(testing_set[0][0]))

vader_correct = 0
vote_correct = 0

for doc in testing_set:
    vader_analysis = sid.polarity_scores(doc)
    vote_analysis = s.sentiment(doc)
    if vader_analysis['compound'] > 0:
        vader_correct += 1

    if vote_analysis[0] == 'pos':
        vote_correct += 1

# for doc in testing_set:
#     vader_analysis = sid.polarity_scores(doc[0])
#     vote_analysis = s.sentiment(doc[0])
#     if vader_analysis['compound'] > 0 and doc[1] == 'pos':
#         vader_correct += 1
#     elif vader_analysis['compound'] < 0 and doc[1] == 'neg':
#         vader_correct += 1
#
#     if vote_analysis[0] == 'pos' and doc[1] == 'pos':
#         vote_correct += 1
#     elif vote_analysis[0] == 'neg' and doc[1] == 'neg':
#         vote_correct += 1

print('Vader accuracy:', str((vader_correct / 46) * 100) + '%')
print('VoteClassifier accuracy:', str((vote_correct / 46) * 100) + '%')

# print(s.sentiment("I'M SHAKING LET'S GOOOOOOOOOOOOOOOOO CELTICS #CUsRise #Celtics"))