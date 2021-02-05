import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
from loguru import logger

def authenticate_twitter_app():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    return auth

class TwitterClient(object):

    def __init__(self, twitter_user):
        self.auth = authenticate_twitter_app()
        self.twitter_client = tweepy.API(self.auth)
        self.twitter_user = twitter_user

    def get_user_timeline_unseen_tweets(self, last_seen_id):
        unseen_tweets = []
        for tweet in tweepy.Cursor(self.twitter_client.user_timeline,
                                   screen_name=self.twitter_user,
                                   since_id=last_seen_id,
                                   tweet_mode="extended").items():
            unseen_tweets.append(tweet)
        return unseen_tweets

    def _favorite_tweet(self, tweet_id):
        try:
            self.twitter_client.create_favorite(tweet_id)
            logger.info(f"favorite the status: {tweet_id}")
        except tweepy.error.TweepError as e:
            logger.warning(f"{e}: {tweet_id}")

    def _retweet_tweet(self, tweet_id):
        try:
            self.twitter_client.retweet(tweet_id)
            logger.info(f"retweet the status: {tweet_id}")
        except tweepy.error.TweepError as e:
            logger.warning(f"{e}: {tweet_id}")

    def favorite_and_retweet(self, tweets, filter_word=""):
        for tweet in tweets:
            if filter_word in tweet.full_text:
                self._favorite_tweet(tweet.id)
                self._retweet_tweet(tweet.id)