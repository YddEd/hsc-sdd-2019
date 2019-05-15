import tweepy
import json
from pathlib import Path


def openFile(filePath, searchMoves):
    fileFolder = Path(filePath)
    f = open(fileFolder, "w")
    with f as outfile:
        json.dump(searchMoves, outfile, indent=4)
    f.close()


# Twitter authentication with Tweepy
def authentication(consumerKey, consumerSecret, accessToken, accessTokenSecret):
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    return api


def search(api, query):  # Search for a tweet with a specific query
    searchMoves = api.search(q=query, count=100)
    return searchMoves
