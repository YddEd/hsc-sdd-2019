import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import json
from pathlib import Path


class myStreamListener(StreamListener):  # Stream listener to check for tweets
    def on_data(self, data):
        print(data)
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
