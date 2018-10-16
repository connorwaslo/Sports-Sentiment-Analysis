import tweepy
import json

with open('json/twitter_credentials.json', 'r') as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='#celtics', f='tweets').items(30):
    if not tweet.retweeted and 'RT @' not in tweet.text:
        print(tweet.text)
        print('-----\n')