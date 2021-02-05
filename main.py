from config import screen_data, update_last_seen_id
from twitter import TwitterClient

def twitter():
    for account in screen_data["twitter"]:
        (_, details), = account.items()
        twitter_client = TwitterClient(details["screen_name"])
        unseen_tweets = twitter_client.get_user_timeline_unseen_tweets(details["last_seen_id"])
        twitter_client.favorite_and_retweet(unseen_tweets, filter_word=details.get("filter_word", ""))

        if unseen_tweets:
            details["last_seen_id"] = unseen_tweets[0].id
            update_last_seen_id(screen_data)

def main():
    twitter()

if __name__ == '__main__':
    main()