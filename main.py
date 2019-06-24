import twitter
import lichess
from tweepy import Stream
from tweepy import StreamListener
import json
import os
import credentials


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


if __name__ == "__main__":
    # Tokens go here, I'm using environment variables for mine
    lichess_token = credentials.lichess_token
    file_path = os.environ["sddFilePath"]
    query_list = ["bwbchess"]
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = twitter.twitter_streamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, query_list)
