from config import *
from twitter import action
import schedule, time

def main():
    tweets = API.user_timeline(screen_name=NANASE_TWITTER_NAME, tweet_mode="extended")

    unseen_tweets = []
    for tweet in tweets:
        if NANASE_TWITTER_LAST_SEEN_ID == tweet.id:
            break
        else:
            unseen_tweets.append(tweet)

    if unseen_tweets:
        # the first element is the last seen id
        set_nanase_twitter_last_seen_id(unseen_tweets[0].id)

        for tweet in unseen_tweets:
            action(API.create_favorite, tweet.id, "favorite")
            action(API.retweet, tweet.id, "retweet")

if __name__ == '__main__':
    schedule.every(1).hours.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)