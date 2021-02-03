from os import environ
from yaml import safe_load

CONSUMER_KEY = environ.get("CONSUMER_KEY")
CONSUMER_SECRET = environ.get("CONSUMER_SECRET")
ACCESS_KEY = environ.get("ACCESS_KEY")
ACCESS_SECRET = environ.get("ACCESS_SECRET")

with open("screen.yaml", "r") as stream:
    data = safe_load(stream)

NANASE_TWITTER = data["nanase_twitter"]
WORK_RELATED_TWITTER = data["work_related_twitter"]
