from config import NANASE_TWITTER_NAME, NANASE_TWITTER_LAST_SEEN_ID, set_nanase_twitter_last_seen_id
from twitter import TwitterClient

def main():
    twitter_client = TwitterClient(NANASE_TWITTER_NAME)
    unseen_tweets = twitter_client.get_user_timeline_unseen_tweets(NANASE_TWITTER_LAST_SEEN_ID)
    twitter_client.favorite_tweets(unseen_tweets)
    twitter_client.retweet_tweets(unseen_tweets)

    set_nanase_twitter_last_seen_id(unseen_tweets)

if __name__ == '__main__':
    main()