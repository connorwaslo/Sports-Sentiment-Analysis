import nltk
import random
import pickle
import csv
import re

from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

from nltk.tokenize import word_tokenize

pos_tweets = []
with open('training_data/positive_tweets.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        tweet = row[0]
        pos_tweets.append(re.sub('&.+?;', '', tweet)) # Delete words like &quot;

neg_tweets = []
with open('training_data/negative_tweets.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        tweet = row[0]
        neg_tweets.append(re.sub('&.+?;', '', tweet)) # Delete words like &quot;

all_words = []
documents = []

allowed_word_types = ['J'] # Just adjectives allowed

for p in pos_tweets:
    documents.append((p, 'pos'))
    words = word_tokenize(p)
    part_of_speech = nltk.pos_tag(words)

    for word in part_of_speech:
        all_words.append(word[0].lower())

for p in neg_tweets:
    documents.append((p, 'neg'))
    words = word_tokenize(p)
    part_of_speech = nltk.pos_tag(words)

    for word in part_of_speech:
        all_words.append(word[0].lower())

random.shuffle(documents)

# Save documents
# save_docs = open('pickles/documents.pickle', 'wb')
# pickle.dump(documents, save_docs)
# save_docs.close()

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]

# save_word_features = open('pickles/word_features5k.pickle', 'wb')
# pickle.dump(word_features, save_word_features)
# save_word_features.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


featuresets = [(find_features(rev), category) for (rev, category) in documents[:5000]]

# save_featuresets = open("pickles/featuresets.pickle", "wb")
# pickle.dump(featuresets[:1200], save_featuresets)
# save_featuresets.close()

training_set = featuresets[:4500]
testing_set = featuresets[4500:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("NaiveBayes_classifier accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

LogisticRegression_classifier = SklearnClassifier(LogisticRegression()).train(training_set)
# LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

SGDClassifier_classifier = SklearnClassifier(SGDClassifier()).train(training_set)
# LogisticRegression_classifier.train(training_set)
print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

SVC_classifier = SklearnClassifier(SVC()).train(training_set)
# LogisticRegression_classifier.train(training_set)
print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

LinearSVC_classifier = SklearnClassifier(LinearSVC()).train(training_set)
# LogisticRegression_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

NuSVC_classifier = SklearnClassifier(NuSVC()).train(training_set)
# LogisticRegression_classifier.train(training_set)
print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)
