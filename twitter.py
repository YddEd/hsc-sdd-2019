import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import json
from pathlib import Path


def authentication(consumer_key, consumer_secret):  # Twitter authentication with Tweepy
    auth = OAuthHandler(consumer_key, consumer_secret)
    return auth


def api(auth, access_token, access_token_secret):  # API authenticaiton
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    return api
