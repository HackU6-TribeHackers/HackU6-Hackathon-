import googlemaps


def getGeocode(GOOGLE_KEY):

	# get the user's current location for the google maps API
	location = input("Where are you currently located : ")
	radius = input("How many miles of a radius would you like to search : ")

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