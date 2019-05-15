import twitter
import json
import os
consumerKey = os.environ["sddConsumerKey"]
consumerSecret = os.environ["sddConsumerSecret"]
accessToken = os.environ["sddAccessToken"]
accessTokenSecret = os.environ["sddAccessTokenSecret"]
filePath = os.environ["sddFilePath"]
twitter.authentication(consumerKey, consumerSecret,
                       accessToken, accessTokenSecret)
query = "#bwbchess"
api = twitter.authentication(
    consumerKey, consumerSecret, accessToken, accessTokenSecret)
# Search for tweets containing the hashtag #bwbchess
searchMoves = twitter.search(api, query)
# Pretty print the response into a file. Mainly used just for me to figure out the JSON.
twitter.openFile(filePath, searchMoves)
jsonMoves = json.loads(json.dumps(searchMoves))
userMentions = jsonMoves["statuses"][0]["entities"]["user_mentions"][0]["screen_name"]
