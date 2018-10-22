import tweepy
import json
import unicodedata
import time

with open('json/twitter_credentials.json', 'r') as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
api = tweepy.API(auth)

knicks = []
mavs = []

iter = 0

while iter < 3:
    for tweet in tweepy.Cursor(api.search, q='#knicks', f='tweets', tweet_mode='extended').items(90):
        if not tweet.retweeted and 'RT @' not in tweet.full_text:
            print(tweet.full_text)
            knicks.append(
                unicodedata.normalize('NFKD', tweet.full_text).encode('ascii', 'ignore').decode('utf-8') + '\n***\n'
            )
    for tweet in tweepy.Cursor(api.search, q='#mavs', f='tweets', tweet_mode='extended').items(90):
        if not tweet.retweeted and 'RT @' not in tweet.full_text:
            print(tweet.full_text)
            mavs.append(
                unicodedata.normalize('NFKD', tweet.full_text).encode('ascii', 'ignore').decode('utf-8') + '\n***\n'
            )

    time.sleep(902)
    iter += 1

# Save tweets to text file for manual classification
with open('tweets/knicks.txt', 'w') as f:
    for t in knicks:
        f.write(t)

with open('tweets/mavs.txt', 'w') as f:
    for t in mavs:
        f.write(t)