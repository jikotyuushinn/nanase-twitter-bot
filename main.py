from config import *
from twitter import action
import tweepy
from loguru import logger

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name=NANASE_TWITTER, tweet_mode="extended", count=100)

for tweet in tweets:
    # print(tweet.created_at, end=" ")
    # print(tweet.id)
    # print(tweet.full_text)
    action(api.create_favorite, tweet.id)
    action(api.retweet, tweet.id)

