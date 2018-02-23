import requests
import json
import tweepy
import googlemaps
# from twitter_data import getTwitterData
# from geocoding import getGeocode


CITY_NEEDED = [0, 7, 10, 11, 12, 14]



"""Function to get all of the relevant tweets"""
def getTwitterData(api, key_phrases, geocode_string, target_city):

	# create arrays to hold all of the found tweets and their respective users
	# all_tweets_text = []
	# all_tweet_users = []
	all_tweets = []

	num_tweets_to_show = 10

	for index in range(len(key_phrases)):

		if index >= 5:
			num_tweets_to_show = 5

		elif index >= 10:
			num_tweets_to_show = 3

		target_str = key_phrases[index]

		if index in CITY_NEEDED:
			target_str += ' ' + target_city
			searches = api.search(q=target_str, count=num_tweets_to_show)

		# searches = api.search(q=["buying :) OR buying new home OR new home :) OR home :( OR new home OR moving to " + str(target_city)], geocode = geocode_string count=50)
		else:
			searches = api.search(q=target_str, geocode=geocode_string, count=num_tweets_to_show)

		for tweet in searches:	
			tweet_data = tweet._json
			# pprint.pprint(tweet_data)
			tweet_text = tweet_data['text']
			tweet_user = tweet_data['user']['screen_name']
			
			if not tweet_text.startswith('RT ', 0, 3):
				# print ("%s : %s" % (tweet_user, tweet_text))
				# all_tweets_text.append(tweet_text)
				# all_tweet_users.append(tweet_user)
				tweet = tweet_user + ' : ' + tweet_text
				all_tweets.append(tweet)

	return all_tweets


"""Function to get the geocode for the location"""
def getGeocode(GOOGLE_KEY, location, radius):

	# # get the user's current location for the google maps API
	# location = input("Where are you currently located : ")
	# radius = input("How many miles of a radius would you like to search : ")

	gmaps = googlemaps.Client(key=GOOGLE_KEY)

	geocode = gmaps.geocode(location)

	# get all relevant information to create the geocode string
	formatted_address = geocode[0]['formatted_address'].split(',')
	target_city = formatted_address[len(formatted_address) - 3]

	coordinates = geocode[0]['geometry']['location']
	latitude = str(coordinates['lat'])
	longitude = str(coordinates['lng'])

	geocode_string = latitude + ',' + longitude + ',' + radius + 'mi'

	return geocode_string, target_city



# get the previously selected key phrases from the file containg them
def mainReceiver(location, radius):
	key_phrases = []
	with open("requirements/key-phrases.txt", "r") as phrases_file:
		for line in phrases_file:
			line = line.strip('\n')
			key_phrases.append(line)
	# print(key_phrases)

	# load the api keys data from the json file
	with open("requirements/api-keys.json", "r") as api_keys:
		api_keys_json = json.load(api_keys)

	# google authentication key
	GOOGLE_KEY = api_keys_json['google_api_key']

	# all of the twitter authentication keys
	CONSUMER_KEY = api_keys_json['twitter_consumer_key']
	CONSUMER_SECRET = api_keys_json['twitter_consumer_secret']
	ACCESS_TOKEN = api_keys_json['twitter_access_token']
	ACCESS_SECRET = api_keys_json['twitter_access_secret']

	geocode_string, target_city = getGeocode(GOOGLE_KEY, location, radius)

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

	api = tweepy.API(auth)


	tweets_list = getTwitterData(api, key_phrases, geocode_string, target_city)

	return tweets_list


# print (len(relevant_tweets_text))
# print (len(relevant_tweets_users))
