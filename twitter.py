import tweepy
from loguru import logger

def action(func, tweet_id, func_name):
    try:
        func(tweet_id)
        logger.info(f"{func_name} the status: {tweet_id}")
    except tweepy.error.TweepError as e:
        logger.warning(f"{e}: {tweet_id}")