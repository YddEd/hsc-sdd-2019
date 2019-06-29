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
            move, user_mentions = manipulate_tweet(tweet)
            game_id = lichess.get_game_id(lichess_token)
            make_move(user_mentions, game_id, move)
            return True
        except BaseException as e:
            print(f"Error on_data {str(e)}")
        return True

    def on_error(self, status):
        print(status)
        if status == 420:
            return False


def manipulate_tweet(tweet):
    str_tweet = tweet["text"]
    try:
        split_tweet = str_tweet.split(" ")
        move = str(split_tweet[-1])
        print(f"Move is {move}")
    except IndexError:
        print("Move not found!")
        return False
    try:
        user_mentions = tweet["entities"]["user_mentions"][0]["screen_name"]
    except IndexError:
        print("No user mentions")
        return False
    return move, user_mentions



def make_move(user_mentions, game_id, move):
    if user_mentions == "bwbchess":
        print("Correct user mention")
        lichess.make_move(game_id, move, lichess_token)
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
