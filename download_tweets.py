import tweepy
import json
import unicodedata

with open('json/twitter_credentials.json', 'r') as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
api = tweepy.API(auth)

tweets = []

for tweet in tweepy.Cursor(api.search, q='#celtics', f='tweets', tweet_mode='extended').items(50):
    if not tweet.retweeted and 'RT @' not in tweet.full_text:
        print(tweet.full_text)
        tweets.append(
            unicodedata.normalize('NFKD', tweet.full_text).encode('ascii', 'ignore').decode('utf-8') + '\n***\n'
        )

# Save tweets to text file for manual classification
with open('tweets/celtics.txt', 'w') as f:
    for t in tweets:
        f.write(t)