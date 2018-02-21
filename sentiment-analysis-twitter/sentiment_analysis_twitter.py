# import necessary libraries
import tweepy
from textblob import TextBlob 

# declare auth keys to connect to Twitter API
consumer_key = 'FRE5ox8ZGJ1NNONYMAxWrlBVj'
consumer_secret = 'VS2pldz1Us4vLEIIy6QK7zSnHgglAStDCWZFjui9M8D5uXbCsF'

access_token = '843964382618963969-3KaLYcYFREeTQovYjlJVpyIohZabRJe'
access_token_secret = '3aNBnarRbDvEPx5lEk0fHhGUpO4uIqAYM8Zg4GU4IFQ24'

# Connect to the API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Read tweets from API
public_tweets = api.search('Florida shooting')

# Sentiment analysis on tweets
for tweet in public_tweets:
    print (tweet.text)
    analysis = TextBlob(tweet.text)
    print (analysis.sentiment)

