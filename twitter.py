import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import json
from pathlib import Path
import credentials


class twitter_streamer():
    """
    Class for streaming and processing live tweets.
    """

    def stream_tweets(self, fetched_tweets_filename, query_list):
        # Handles Authentication and connection to Twitter and their Streaming API
        listener = myStreamListener(fetched_tweets_filename)
        stream = Stream(auth, listener)
        stream.filter(track=query_list)  # Filter tweets based on keywords


class myStreamListener(StreamListener):
    """
    Stream listener to check for and print tweets
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, "a") as outfile:
                json.dump(json.loads(data), outfile, indent=4)
            return True
        except BaseException as e:
            print(f"Error on_data {str(e)}")
        return True

    def on_error(self, status):
        print(status)


def open_file(file_path, search_moves):  # Write json to a file
    file_folder = Path(file_path)
    f = open(file_folder, "w")
    with f as outfile:
        json.dump(search_moves, outfile, indent=4)
    f.close()


# Twitter authentication with Tweepy
def authentication(consumer_key, consumer_secret):
    auth = OAuthHandler(consumer_key, consumer_secret)
    return auth


def api(auth, access_token, access_token_secret):
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    return api


def search(api, query):  # Search for a tweet with a specific query
    search_moves = api.search(q=query, count=100)
    return search_moves


auth = authentication(credentials.consumer_key, credentials.consumer_secret)
api = api(auth, credentials.access_token, credentials.access_token_secret)
