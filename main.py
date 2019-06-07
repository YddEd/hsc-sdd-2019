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
# twitter.openFile(file_path, searchMoves)


def get_move(json_tweet):  # Split the tweet to get the move
    try:
        str_tweet = json_tweet["statuses"][0]["text"]
        split_tweet = str_tweet.split(" ")
        move = str(split_tweet[-1])
        return move
    except IndexError:
        print("Move not found!")
        return False


def tweet_query(query):
    latest_tweet = twitter.search(api, query)
    json_tweet = json.loads(json.dumps(latest_tweet))
    return json_tweet


def user_mentions(tweet_data):
    try:  # Get the first mention in the tweet
        print(f"Move is: {move}")
        user_mentions = tweet_data["statuses"][0]["entities"]["user_mentions"][0]["screen_name"]
        print(f"User mention is: {user_mentions}")
        return user_mentions
    except IndexError:
        print("No user mentions")
        return False


def make_move():
    if user_mention == "bwbchess":
        print("Correct user mention")
        lichess.make_move(game_id, move, lichess_token)
    else:
        print(user_mention)
        print("Something bad happened and a move was not made!")


tweet_data = tweet_query("#bwbchess")
if get_move(tweet_data) != False:
    move = get_move(tweet_data)
    user_mention = user_mentions(tweet_data)
    game_id = lichess.get_game_id(lichess_token)
    make_move()
else:
print("Game, move and user mention not found!")
