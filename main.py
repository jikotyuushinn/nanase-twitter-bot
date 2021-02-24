from twitter import TwitterClient
from firebase import Firebase

def twitter():
    f = Firebase("Twitter")
    docs = f.get_stream()

    for doc in docs:
        doc_id = doc.id
        doc = doc.to_dict()
        twitter_client = TwitterClient(doc["screen_name"])
        unseen_tweets = twitter_client.get_user_timeline_unseen_tweets(doc["last_seen_id"])
        is_succeeded = twitter_client.favorite_and_retweet(unseen_tweets,
                                                           filter_word=doc.get("filter_word", ""))

        if unseen_tweets and is_succeeded:
             doc["last_seen_id"] = unseen_tweets[0].id
             f.update(doc_id, doc)

def main():
    twitter()

if __name__ == '__main__':
    main()