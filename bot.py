import tweepy

api_key = ""
api_key_secret = ""
bearer_token = r""
access_token = ""
access_token_secret = ""


# Establishing a connection with Twitter API
client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# client.create_tweet(text= "Hello, Twitter API")
client.create_tweet(text = "yes")
