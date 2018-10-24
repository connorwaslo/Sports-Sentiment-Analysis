import pickle
import random

from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        decision_votes = votes.count(mode(votes))
        confidence = decision_votes / len(votes)

        return confidence


documents_f = open('pickles/documents.pickle', 'rb')
documents = pickle.load(documents_f)
documents_f.close()

word_features5k_f = open('pickles/word_features5k.pickle', 'rb')
word_features = pickle.load(word_features5k_f)
word_features5k_f.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


featuresets_f = open('pickles/featuresets_5k.pickle', 'rb')
featuresets = pickle.load(featuresets_f)
featuresets_f.close()

random.shuffle(featuresets)
print(len(featuresets))

training_set = featuresets[:4500]
testing_set = featuresets[4500:]

open_file = open('pickles/classifiers/naive_bayes_classifier.pickle', 'rb')
classifier = pickle.load(open_file)
open_file.close()

open_file = open('pickles/classifiers/logistic_classifier.pickle', 'rb')
LogisticRegression_classifier = pickle.load(open_file)
open_file.close()

open_file = open('pickles/classifiers/linear_svc_classifier.pickle', 'rb')
LinearSVC_classifier = pickle.load(open_file)
open_file.close()

open_file = open('pickles/classifiers/sgdc_classifier.pickle', 'rb')
SGDC_classifier = pickle.load(open_file)
open_file.close()

open_file = open('pickles/classifiers/nusvc_classifier.pickle', 'rb')
NuSVC_classifier = pickle.load(open_file)
open_file.close()

open_file = open('pickles/classifiers/svc_classifier.pickle', 'rb')
SVC_classifier = pickle.load(open_file)
open_file.close()

voted_classifier = VoteClassifier(classifier,
                                  # LinearSVC_classifier,
                                  LogisticRegression_classifier,
                                  NuSVC_classifier,
                                  # SGDC_classifier,
                                  # SVC_classifier
                                  )


def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats), voted_classifier.confidence(feats)
