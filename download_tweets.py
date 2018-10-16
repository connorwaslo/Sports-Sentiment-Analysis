import tweepy
import json
import unicodedata
import time

with open('json/twitter_credentials.json', 'r') as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
api = tweepy.API(auth)

celtics = []
sixers = []

iter = 0

while iter < 3:
    for tweet in tweepy.Cursor(api.search, q='#celtics', f='tweets', tweet_mode='extended').items(90):
        if not tweet.retweeted and 'RT @' not in tweet.full_text:
            print(tweet.full_text)
            celtics.append(
                unicodedata.normalize('NFKD', tweet.full_text).encode('ascii', 'ignore').decode('utf-8') + '\n***\n'
            )
    for tweet in tweepy.Cursor(api.search, q='#sixers', f='tweets', tweet_mode='extended').items(90):
        if not tweet.retweeted and 'RT @' not in tweet.full_text:
            print(tweet.full_text)
            sixers.append(
                unicodedata.normalize('NFKD', tweet.full_text).encode('ascii', 'ignore').decode('utf-8') + '\n***\n'
            )

    time.sleep(902)
    iter += 1

# Save tweets to text file for manual classification
with open('tweets/celtics.txt', 'w') as f:
    for t in celtics:
        f.write(t)

with open('tweets/sixers.txt', 'w') as f:
    for t in sixers:
        f.write(t)