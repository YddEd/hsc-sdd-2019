import tweepy
from tweepy import OAuthHandler
import json
from pathlib import Path


def open_file(file_path, search_moves):
    file_folder = Path(file_path)
    f = open(file_folder, "w")
    with f as outfile:
        json.dump(search_moves, outfile, indent=4)
    f.close()


# Twitter authentication with Tweepy
def authentication(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    return api


def search(api, query):  # Search for a tweet with a specific query
    search_moves = api.search(q=query, count=100)
    return search_moves
