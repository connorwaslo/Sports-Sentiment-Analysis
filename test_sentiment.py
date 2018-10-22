import sentiment_analyzer as s
import pickle

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

# Test accuracy of Vader sentiment analysis
documents_f = open('pickles/documents.pickle', 'rb')
documents = pickle.load(documents_f)
documents_f.close()

# Use same testing set as other classifiers
testing_set = documents[:1000]

correct = 0

for doc in testing_set:
    analysis = sid.polarity_scores(doc[0])
    if analysis['compound'] > 0 and doc[1] == 'pos':
        correct += 1
    elif analysis['compound'] < 0 and doc[1] == 'neg':
        correct += 1

print('Accuracy:', str((correct / 1000) * 100) + '%')

# print(s.sentiment("I'M SHAKING LET'S GOOOOOOOOOOOOOOOOO CELTICS #CUsRise #Celtics"))