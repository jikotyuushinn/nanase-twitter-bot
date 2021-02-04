from os import environ
from yaml import safe_load, safe_dump
import tweepy

CONSUMER_KEY= environ.get("CONSUMER_KEY")
CONSUMER_SECRET = environ.get("CONSUMER_SECRET")
ACCESS_KEY = environ.get("ACCESS_KEY")
ACCESS_SECRET = environ.get("ACCESS_SECRET")
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
API = tweepy.API(auth)

with open("screen.yaml", "r") as stream:
    screen_data = safe_load(stream)

NANASE_TWITTER_NAME = screen_data["nanase_twitter"]["name"]
NANASE_TWITTER_LAST_SEEN_ID = screen_data["nanase_twitter"]["last_seen_id"]
WORK_RELATED_TWITTER = screen_data["work_related_twitter"]

def set_nanase_twitter_last_seen_id(twitter_id):
    screen_data["nanase_twitter"]["last_seen_id"] = twitter_id
    with open("screen.yaml", "w") as s:
        safe_dump(screen_data, s)


