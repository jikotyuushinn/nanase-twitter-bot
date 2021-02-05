from os import environ
from yaml import safe_load, safe_dump

CONSUMER_KEY= environ.get("CONSUMER_KEY")
CONSUMER_SECRET = environ.get("CONSUMER_SECRET")
ACCESS_KEY = environ.get("ACCESS_KEY")
ACCESS_SECRET = environ.get("ACCESS_SECRET")

with open("screen.yaml", "r") as stream:
    screen_data = safe_load(stream)

def update_last_seen_id(data):
    with open("screen.yaml", "w", encoding="utf-8") as s:
        safe_dump(data, s, allow_unicode=True)