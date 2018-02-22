import requests
import json
import tweepy
import googlemaps

# load the api keys data from the json file
with open("api-keys.json", "r") as api_keys:
	api_keys_json = json.load(api_keys)

# google authentication keys
GOOGLE_KEY = api_keys_json['google_api_key']

# all of the twitter authentication keys
CONSUMER_KEY = api_keys_json['twitter_consumer_key']
CONSUMER_SECRET = api_keys_json['twitter_consumer_secret']
ACCESS_TOKEN = api_keys_json['twitter_access_token']
ACCESS_SECRET = api_keys_json['twitter_access_secret']

location = input("Where are you currently located : ")
# radius = input("How many miles of a radius would you like to search : ")

gmaps = googlemaps.Client(key=GOOGLE_KEY)

geocode = gmaps.geocode(location)

formatted_address = geocode[0]['formatted_address'].split(',')
target_city = formatted_address[len(formatted_address) - 3]

# coordinates = geocode[0]['geometry']['location']
# latitude = str(coordinates['lat'])
# longitude = str(coordinates['lng'])

# geocode_string = latitude + ',' + longitude + ',' + radius + 'mi'
target_str = "moving to " + target_city + " :)"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

# searches = api.search(q=["buying :) OR buying new home OR new home :) OR home :( OR new home OR moving to " + str(target_city)], geocode = geocode_string count=50)
searches = api.search(q=target_str, count=50)

json_tweets = []
for tweet in searches:
	# json_tweets.append(json.dumps(tweet._json))
	# print (json_data)
	# print (str(tweet))
	tweet_data = tweet._json
	print("%s : %s" % (tweet_data['user']['screen_name'], tweet_data['text']))
	print()


		
