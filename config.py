from os import environ
from yaml import safe_load, safe_dump
import tweepy

CONSUMER_KEY= environ.get("CONSUMER_KEY", default="xhawhVNqRgMCyEDKOOTny30wr")
CONSUMER_SECRET = environ.get("CONSUMER_SECRET", default="Q4ePr6q11jV307v9PBxhP8ppsj8MrJZlpilMNc6JovPbdBEQvP")
ACCESS_KEY = environ.get("ACCESS_KEY", default="1356569955450245120-WRz5SEB9ZARcYlJvwXp61Vh2qVYDlE")
ACCESS_SECRET = environ.get("ACCESS_SECRET", default="jzNAvcnXzsQM6gjotij4h6N8U1FnyUpg1fJgHqycXBrPE")

with open("screen.yaml", "r") as stream:
    screen_data = safe_load(stream)

NANASE_TWITTER_NAME = screen_data["nanase_twitter"]["name"]
NANASE_TWITTER_LAST_SEEN_ID = screen_data["nanase_twitter"]["last_seen_id"]
WORK_RELATED_TWITTER = screen_data["work_related_twitter"]

def set_nanase_twitter_last_seen_id(unseen_tweets):
    if unseen_tweets:
        screen_data["nanase_twitter"]["last_seen_id"] = unseen_tweets[0].id
        with open("screen.yaml", "w") as s:
            safe_dump(screen_data, s)


