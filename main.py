from twitter import TwitterClient
from firebase import Firebase

def twitter():
    f = Firebase("Twitter")
    ref = f.get_stream()
    print(ref)

    for item in ref:
        print(item)
        account = f.get(item)
        twitter_client = TwitterClient(account["screen_name"])
        unseen_tweets = twitter_client.get_user_timeline_unseen_tweets(account["last_seen_id"])
        is_succeeded = twitter_client.favorite_and_retweet(unseen_tweets,
                                                           filter_word=account.get("filter_word", ""))

        if unseen_tweets and is_succeeded:
            account["last_seen_id"] = unseen_tweets[0].id
            f.update(item, account)

def main():
    twitter()

if __name__ == '__main__':
    main()