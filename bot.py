import tweepy

api_key = "nI91vHpbiqw04221mLI1v6olv"
api_key_secret = "F3PMOTaH717v03TEcu45plP0mTcpIxEQjRTetNQXAMzD2zW1PD"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAMBQmwEAAAAATXEkOQ%2F6SgIRCquwRR0F3n9kkIE%3DI0KGDn8vvAQLczIyZFUGQz759CLF9TIqKZEKOlgZV19d596V7n"
access_token = "957524978118770690-aKakkA0hrvNyUJQDKinPn2L3of33cTV"
access_token_secret = "Kjy3Nqx2MZqOTJHdqE41XyPc3wnXq5bUH3BoN4NdOyoCk"


# Establishing a connection with Twitter API
client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

client.create_tweet(text= "Hello, Twitter API")