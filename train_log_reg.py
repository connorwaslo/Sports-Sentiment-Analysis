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
save_docs = open('pickles/documents.pickle', 'wb')
pickle.dump(documents, save_docs)
save_docs.close()

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]

# Save features
save_word_features = open('pickles/word_features5k.pickle', 'wb')
pickle.dump(word_features, save_word_features)
save_word_features.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


featuresets = [(find_features(rev), category) for (rev, category) in documents[:5000]]

# Save featuresets
save_featuresets = open("pickles/featuresets_5k.pickle", "wb")
pickle.dump(featuresets[:1200], save_featuresets)
save_featuresets.close()

training_set = featuresets[:4500]
testing_set = featuresets[4500:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("NaiveBayes_classifier accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

# Save NB Classifier
save_naive = open('pickles/classifiers/naive_bayes_classifier.pickle', 'wb')
pickle.dump(classifier, save_naive)
save_naive.close()

LogisticRegression_classifier = SklearnClassifier(LogisticRegression()).train(training_set)
# LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

# Save Logistic Regression Classifier
save_logistic = open('pickles/classifiers/logistic_classifier.pickle', 'wb')
pickle.dump(LogisticRegression_classifier, save_logistic)
save_logistic.close()

SGDClassifier_classifier = SklearnClassifier(SGDClassifier()).train(training_set)
# LogisticRegression_classifier.train(training_set)
print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

# Save SGDClassifier
save_sgdc = open('pickles/classifiers/sgdc_classifier.pickle', 'wb')
pickle.dump(SGDClassifier_classifier, save_sgdc)
save_sgdc.close()

SVC_classifier = SklearnClassifier(SVC()).train(training_set)
# LogisticRegression_classifier.train(training_set)
print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

# Save SVC
save_svc = open('pickles/classifiers/svc_classifier.pickle', 'wb')
pickle.dump(SVC_classifier, save_svc)
save_svc.close()

LinearSVC_classifier = SklearnClassifier(LinearSVC()).train(training_set)
# LogisticRegression_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

# Save Linear SVC
save_linear_svc = open('pickles/classifiers/linear_svc_classifier.pickle', 'wb')
pickle.dump(LinearSVC_classifier, save_linear_svc)
save_linear_svc.close()

NuSVC_classifier = SklearnClassifier(NuSVC()).train(training_set)
# LogisticRegression_classifier.train(training_set)
print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

# Save NuSVC
save_nusvc = open('pickles/classifiers/nusvc_classifier.pickle', 'wb')
pickle.dump(NuSVC_classifier, save_nusvc)
save_nusvc.close()
