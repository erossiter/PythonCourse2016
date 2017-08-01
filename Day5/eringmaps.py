# pip install googlemaps
#https://console.developers.google.com/apis/credentials?project=_
#need maps and distance APIs enabled
import googlemaps

import imp
gmaps = imp.load_source('gmaps', '/Users/erinrossiter/Dropbox/Summer2016/googleKeys.py')

#gmaps = googlemaps.Client(api_key)
dir(gmaps)
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
location=gmaps.gmaps.geocode(whitehouse)
#print location
#print location[0]
#print location[0]['geometry']['location']
latlng=location[0]['geometry']['location']
lat, lng=latlng.values()
#print lat
#print lng

#destination = gmaps.gmaps.reverse_geocode(latlng)
#print destination 


duke = gmaps.gmaps.geocode('326 Perkins Library, Durham, NC 27708')
duke=duke[0]['geometry']['location']

washU = gmaps.gmaps.geocode('1 Brookings Dr, St. Louis, MO 63130')
washU=washU[0]['geometry']['location']
#distance = gmaps.gmaps.distance_matrix(duke, latlng)
#print distance['rows'][0]['elements'][0]['distance']['text']
#print distance['rows'][0]['elements'][0]['distance']['value']

whiteHouse = latlng
otherPlaces = [whiteHouse, duke, washU]

embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]

print embassies[0]
print whiteHouse

def myFunc(set1, set2):
	if len(set1) != len(set2):
		raise "Can't compare lists of different lengths."
	if type(set1) is list:
		for i in range(0, len(set1)):
			place1 = set1[i]
			place2 = set2[i]
	else:
		place1 = set1
		place2 = set2
	distance = gmaps.gmaps.distance_matrix(place1, place2)
	print distance['rows'][0]['elements'][0]['distance']['value']

myFunc(latlng, duke)
myFunc(otherPlaces, embassies)



# TODO: write code to answer the following questions: 
# which embassy is closest to the White House in meters? how far? 
# what is its address? You will get errors - debug
# if I wanted to hold a morning meeting there, which cafe would you suggest?
# if I wanted to hold an evening meeting there, which bar would you suggest? 

