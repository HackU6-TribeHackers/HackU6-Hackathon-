import requests
import json
import tweepy
import googlemaps
from twitter_data import getTwitterData


CITY_NEEDED = [0, 7, 10, 11, 12, 14]

# get the previously selected key phrases from the file containg them
key_phrases = []
with open("requirements/key-phrases.txt", "r") as phrases_file:
	for line in phrases_file:
		line = line.strip('\n')
		key_phrases.append(line)
# print(key_phrases)

# load the api keys data from the json file
with open("../api-keys.json", "r") as api_keys:
	api_keys_json = json.load(api_keys)

# google authentication keys
GOOGLE_KEY = api_keys_json['google_api_key']

# all of the twitter authentication keys
CONSUMER_KEY = api_keys_json['twitter_consumer_key']
CONSUMER_SECRET = api_keys_json['twitter_consumer_secret']
ACCESS_TOKEN = api_keys_json['twitter_access_token']
ACCESS_SECRET = api_keys_json['twitter_access_secret']

location = input("Where are you currently located : ")
radius = input("How many miles of a radius would you like to search : ")
print ()

gmaps = googlemaps.Client(key=GOOGLE_KEY)

geocode = gmaps.geocode(location)

formatted_address = geocode[0]['formatted_address'].split(',')
target_city = formatted_address[len(formatted_address) - 3]

coordinates = geocode[0]['geometry']['location']
latitude = str(coordinates['lat'])
longitude = str(coordinates['lng'])

geocode_string = latitude + ',' + longitude + ',' + radius + 'mi'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)


relevant_tweets_text, relevant_tweets_users = getTwitterData(api, key_phrases, geocode_string, target_city, CITY_NEEDED)

print (len(relevant_tweets_text))
print (len(relevant_tweets_users))