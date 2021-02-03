from config import *
import tweepy
from loguru import logger

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name="nanase_andstaff", tweet_mode="extended", count=100)

for tweet in tweets:
    # print(tweet.created_at, end=" ")
    # print(tweet.id)
    # print(tweet.full_text)
    try:
        api.create_favorite(tweet.id)
        api.retweet(tweet.id)
        logger.info(f"favorite the status: {tweet.id}")
    except tweepy.error.TweepError as e:
        logger.exception(e)
