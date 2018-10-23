import tweepy
import json
import unicodedata
import time
import csv

with open('json/twitter_credentials.json', 'r') as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
api = tweepy.API(auth)

# knicks = []
# mavs = []

tweets = []

iter = 0

for tweet in tweepy.Cursor(api.search, q='#gsw', f='tweets', tweet_mode='extended',
                           since='2018-10-21', until='2018-10-23', lang='en').items():
    if iter == 179:
        with open('tweets/warriors.csv', 'a') as f:
            writer = csv.writer(f)
            for t in tweets:
                writer.writerow([t])

        # Empty tweets list
        tweets = []

        time.sleep(901)
        iter = 0

    print(tweet.full_text)
    tweets.append(
        unicodedata.normalize('NFKD', tweet.full_text).encode('ascii', 'ignore').decode('utf-8') + '\n***\n'
    )

    iter += 1

if len(tweets) > 0:
    with open('tweets/warriors.csv', 'a') as f:
        writer = csv.writer(f)
        for t in tweets:
            writer.writerow([t])

# while iter < 3:
#     for tweet in tweepy.Cursor(api.search, q='#knicks', f='tweets', tweet_mode='extended').items(90):
#         if not tweet.retweeted and 'RT @' not in tweet.full_text:
#             print(tweet.full_text)
#             knicks.append(
#                 unicodedata.normalize('NFKD', tweet.full_text).encode('ascii', 'ignore').decode('utf-8') + '\n***\n'
#             )
#     for tweet in tweepy.Cursor(api.search, q='#mavs', f='tweets', tweet_mode='extended').items(90):
#         if not tweet.retweeted and 'RT @' not in tweet.full_text:
#             print(tweet.full_text)
#             mavs.append(
#                 unicodedata.normalize('NFKD', tweet.full_text).encode('ascii', 'ignore').decode('utf-8') + '\n***\n'
#             )
#
#     time.sleep(902)
#     iter += 1

# Save tweets to text file for manual classification

# with open('tweets/mavs.txt', 'w') as f:
#     for t in mavs:
#         f.write(t)