from config import screen_data, update_last_seen_id
from twitter import TwitterClient

def twitter():
    for account in screen_data["twitter"]:
        (key, value), = account.items()
        twitter_client = TwitterClient(value["name"])
        unseen_tweets = twitter_client.get_user_timeline_unseen_tweets(value["last_seen_id"])
        twitter_client.favorite_and_retweet(unseen_tweets, filter_word=value.get("filter_word", ""))

        if unseen_tweets:
            value["last_seen_id"] = unseen_tweets[0].id
            update_last_seen_id(screen_data)

def main():
    twitter()

if __name__ == '__main__':
    main()