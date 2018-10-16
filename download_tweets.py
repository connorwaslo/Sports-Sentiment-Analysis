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

# https://twitter.com/search?f=tweets&vertical=news&q=%23celtics&src=typd
# https://twitter.com/search?vertical=news&q=%23celtics&src=typd

# auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
#
# api = tweepy.API(auth)
#
# me = api.me()
# print('Name:', me.name)
#
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)