import tweepy
from loguru import logger

def action(func, tweet_id):
    try:
        func(tweet_id)
        logger.info(f"favorite the status: {tweet_id}")
    except tweepy.error.TweepError as e:
        logger.warning(e)