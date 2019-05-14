import twitter
import json
import os
CONSUMER_KEY = os.environ["SDD_CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["SDD_CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["SDD_ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["SDD_ACCESS_TOKEN_SECRET"]
filepath = os.environ["SDD_FILE_PATH"]
twitter.authentication(CONSUMER_KEY, CONSUMER_SECRET,
                       ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
query = "#bwbchess"
api = twitter.authentication(
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Search for tweets containing the hashtag #bwbchess
searchmoves = twitter.search(api, query)
# Pretty print the response into a file. Mainly used just for me to figure out the JSON.
twitter.open_file(filepath, searchmoves)
jsonmoves = json.loads(json.dumps(searchmoves))
user_mentions = jsonmoves["statuses"][0]["entities"]["user_mentions"][0]["screen_name"]
