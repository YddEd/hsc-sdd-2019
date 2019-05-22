import twitter
import lichess
import tweepy
from tweepy import Stream
import json
import os

# Tokens go here, I'm using environment variables for mine
consumer_key = os.environ["sddConsumerKey"]
consumer_secret = os.environ["sddConsumerSecret"]
access_token = os.environ["sddAccessToken"]
access_token_secret = os.environ["sddAccessTokenSecret"]
lichess_token = os.environ["sddChessToken"]
file_path = os.environ["sddFilePath"]

api = twitter.authentication(
    consumer_key, consumer_secret, access_token, access_token_secret)

# Pretty print the response into a file. Mainly used just for me to figure out the JSON.
#twitter.openFile(file_path, searchMoves)


def search_for_move(query):  # Search for tweets containing the hashtag #bwbchess
    latest_tweet = twitter.search(api, query)
    json_tweet = json.loads(json.dumps(latest_tweet))
    str_tweet = json_tweet["statuses"][0]["text"]
    split_tweet = str_tweet.split(" ")
    move = str(split_tweet[-1])
    return json_tweet, move


game_id = lichess.get_game_id(lichess_token)
json_tweet, move = search_for_move("#bwbchess")
# Get the first mention in the tweet
user_mentions = json_tweet["statuses"][0]["entities"]["user_mentions"][0]["screen_name"]

if user_mentions == "bwbchess":
    lichess.makeMove(game_id, move, lichess_token)
else:
    print("Something bad happened!")
