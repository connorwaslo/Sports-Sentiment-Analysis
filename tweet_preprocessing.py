import csv
import re
import string


class ProcessTweets:
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
        self.processed_tweets = []
        self.process()

    def process(self):
        raw_tweets = self.load_tweets(self.infile)
        for t in raw_tweets:
            self.processed_tweets.append(self.process_tweet(t))

    def process_tweet(self, tweet):
        # Delete url if any exists
        if 'https://' in tweet:
            start = tweet.find('https://')
            tweet = tweet[0:start]

        # Remove punctuation
        punctuation_regex = re.compile('[%s]' % re.escape(string.punctuation))
        tweet = punctuation_regex.sub(' ', tweet)

        # Make the tweet one line with consistent whitespace
        tweet = "".join(tweet.splitlines())
        tweet = re.sub(' +', ' ', tweet)

        # Lowercase
        tweet = tweet.lower()

        return tweet

    def get_tweets(self):
        return self.processed_tweets

    # Load raw tweets
    def load_tweets(self, infile):
        raw_tweets = []
        with open(infile) as f:
            reader = csv.reader(f)
            for row in reader:
                raw_tweets.append(row[0])

        return raw_tweets

    # Save processed tweets in a csv
    def save_tweets(self):
        with open(self.outfile, newline='') as f:
            writer = csv.writer(f)
            for t in self.processed_tweets:
                writer.writerow([t])
