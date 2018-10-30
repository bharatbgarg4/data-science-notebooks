from tweepy import Stream
from tweepy.streaming import StreamListener
import tweepy, json ,re
from textblob import TextBlob

from ../private.py import consumer_key, consumer_secret, access_token, access_token_secret
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

def clean_tweet(tweet): 
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())
  
def get_tweet_sentiment(tweet): 
    analysis = TextBlob(clean_tweet(tweet)) 
    if analysis.sentiment.polarity > 0: 
        return 'positive'
    elif analysis.sentiment.polarity == 0: 
        return 'neutral'
    else: 
        return 'negative'

def twee(tweet):
	print tweet['text']
	print get_tweet_sentiment(tweet['text'])
	print
	print tweet['user']['screen_name'] 
	print tweet['user']['location']
	print tweet['created_at']
	print 
	print '-- '*12+'\n'

class listener(StreamListener):
	def on_data(self, data):
		twee(json.loads(data))
		return True

	def on_error(self, status):
		print status

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["trump"])