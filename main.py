import twitter
import lichess
from tweepy import Stream
from tweepy import StreamListener
import json
import os
import credentials


class twitter_streamer():
    """
    Class for streaming and processing live tweets.
    """

    def stream_tweets(self, fetched_tweets_filename, query_list):
        # Handles Authentication and connection to Twitter and their Streaming API
        listener = twitter_listener(fetched_tweets_filename)
        stream = Stream(auth, listener)
        stream.filter(track=query_list)  # Filter tweets based on keywords


class twitter_listener(StreamListener):
    """
    Stream listener to check for and print tweets
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            tweet = json.loads(data)
            with open(self.fetched_tweets_filename, "a") as outfile:
                json.dump(tweet, outfile, indent=4)
            user_mentions = get_user_mentions(tweet)
            move = get_move(tweet)
            game_id = lichess.get_game_id(lichess_token)
            make_move(user_mentions, tweet, game_id, move)        
            return True
        except BaseException as e:
            print(f"Error on_data {str(e)}")
        return True
    def on_error(self, status):
        print(status)
        if status == 420:
            return False


def get_move(tweet):
    str_tweet = tweet["text"]
    try:
        split_tweet = str_tweet.split(" ")
        move = str(split_tweet[-1])
        print(f"Move is {move}")
        return move
    except IndexError:
        print("Move not found!")
        return False

def verify_last_move(tweet):
    str_tweet = tweet["text"]
    try:
        split_tweet = str_tweet.split(" ")
        last_move = str(split_tweet[-2])
        print(f"User says the computer's last move is: {last_move}")
        return last_move
    except IndexError:
        print("Move not found!")
        return False

def get_user_mentions(tweet):
    try:
        user_mentions = tweet["entities"]["user_mentions"][0]["screen_name"]
        print(f"User mention: {user_mentions}")
        return user_mentions
    except IndexError:
        print("No user mentions")
        return False

def make_move(user_mentions, tweet,  game_id, move):
    if user_mentions == "bwbchess":
        print("Correct user mention")
        if verify_last_move(tweet) == lichess.game_state(game_id, lichess_token).lower():
            lichess.make_move(game_id, move, lichess_token)
        else:
            print("User has not input the correct computer move")
    else:
        print("Something bad happened and a move was not made!")


if __name__ == "__main__":
    # Tokens go here, I'm using environment variables for mine
    lichess_token = credentials.lichess_token
    query_list = ["bwbchess"]
    fetched_tweets_filename = "tweets.json"
    auth = twitter.authentication(credentials.consumer_key,
                                  credentials.consumer_secret)
    api = twitter.api(auth, credentials.access_token,
                      credentials.access_token_secret)
    twitter_streamer = twitter_streamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, query_list)