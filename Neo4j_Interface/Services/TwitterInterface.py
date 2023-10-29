import tweepy

consumer_key = 'hzg5gtqdLjFDaJEAklNNwnvLY'
consumer_secret = '7Q64JncbsJxBvB0ffKL3ZUfm1caq3aIdqAFz4sACyxS04CIaFk'
access_token = '1659876237429334019-o96PdNzPSOIpunf3GEKkWfwkwg3V4t'
access_token_secret = 'XYlrHQHRFJuJbRBnNVPVVZfq118T0lk8yuxHlcw6XTWEU'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create the API object
api = tweepy.API(auth)

def getTweets(tweet_count) :
    username = '1659878118759227392bassim83896'
    tweets = api.user_timeline(screen_name=username, count=tweet_count, tweet_mode='extended')
    return tweets