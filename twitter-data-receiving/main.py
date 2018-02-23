import requests
import json
import tweepy
from twitter_data import getTwitterData
from geocoding import getGeocode


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

# google authentication key
GOOGLE_KEY = api_keys_json['google_api_key']

# all of the twitter authentication keys
CONSUMER_KEY = api_keys_json['twitter_consumer_key']
CONSUMER_SECRET = api_keys_json['twitter_consumer_secret']
ACCESS_TOKEN = api_keys_json['twitter_access_token']
ACCESS_SECRET = api_keys_json['twitter_access_secret']

geocode_string, target_city = getGeocode(GOOGLE_KEY)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)


relevant_tweets_text, relevant_tweets_users = getTwitterData(api, key_phrases, geocode_string, target_city, CITY_NEEDED)

print (len(relevant_tweets_text))
print (len(relevant_tweets_users))