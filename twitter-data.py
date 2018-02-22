import requests
import json
# from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import tweepy

# all of the authentication keys
ACCESS_TOKEN = '1GHD7OZfz2cBQwwHxE4uYfX4A'
ACCESS_SECRET = 'l2jdooUQCAPy4ZPq4D3gPRVHdkvbLf4DN8ESqGAGi7XaPbxUrv'
CONSUMER_KEY = '354636776-WTqfVPcdwx6iuG3yuU0wilr5SdKfJInjvwUIy2ng'
CONSUMER_SECRET = 'p5IHsqmjDT22Gouh7Zvedwj1eCtPDjXWEy0HVfq7bI805' 


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

print (api.get_user("twitter"))

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print (tweet.text)

# oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# twitter_stream = TwitterStream(auth=oauth)

# iterator = twitter_stream.statuses.sample()

# # Print each tweet in the stream to the screen 
# # Here we set it to stop after getting 1000 tweets. 
# # You don't have to set it to stop, but can continue running 
# # the Twitter API to collect data for days or even longer. 
# tweet_count = 1000
# for tweet in iterator:
#     tweet_count -= 1
#     # Twitter Python Tool wraps the data returned by Twitter 
#     # as a TwitterDictResponse object.
#     # We convert it back to the JSON format to print/score
#     print (json.dumps(tweet))  
    
#     # The command below will do pretty printing for JSON data, try it out
#     # print json.dumps(tweet, indent=4)
       
#     if tweet_count <= 0:
#         break 

# # response = requests.get("https://api.twitter.com/1.1/search/tweets.json?q=place%3A07d9cd6afd884001")
# # print (response.status_code)

# # data = json.loads(response)

# # print (json.dumps(data))
