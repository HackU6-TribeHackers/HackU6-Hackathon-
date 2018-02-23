import json
import tweepy

def getTwitterData(api, key_phrases, geocode_string, target_city, CITY_NEEDED):

	# create arrays to hold all of the found tweets and their respective users
	all_tweets_text = []
	all_tweet_users = []

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
				all_tweets_text.append(tweet_text)
				all_tweet_users.append(tweet_user)

	return all_tweets_text, all_tweet_users

