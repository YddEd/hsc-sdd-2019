import tweepy
import json
import os
from pathlib import Path


def open_file():
    file_folder = Path(your_file_path)
    f = open(file_folder, "w")
    with f as outfile:
        json.dump(searchmoves, outfile, indent=4)
    f.close()


CONSUMER_KEY = your_consumer_key
CONSUMER_SECRET = your_consumer_secret
ACCESS_TOKEN = your_access_token
ACCESS_TOKEN_SECRET = your_access_token_secret
# Twitter authentication with Tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
# Search for tweets containing the hashtag #bwbchess
searchmoves = api.search(q="#bwbchess", count=100)
# Pretty print the response into a file. Mainly used just for me to figure out the JSON.
open_file()
