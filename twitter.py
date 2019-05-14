import tweepy
import json
from pathlib import Path


def open_file(filepath, searchmoves):
    file_folder = Path(filepath)
    f = open(file_folder, "w")
    with f as outfile:
        json.dump(searchmoves, outfile, indent=4)
    f.close()


# Twitter authentication with Tweepy
def authentication(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    return api


def search(api, query):  # Search for a tweet with a specific query
    searchmoves = api.search(q=query, count=100)
    return searchmoves
