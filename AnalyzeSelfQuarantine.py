# Larry To
# Created on: 4/10/2020
# Purpose: analyze local quarantine location data and display it on a plot


# Import Libraries
import pickle
import pandas
import googlemaps
import re 

file = open('data/processedData/self_quarantine.pkl', 'rb')
data = pickle.load(file)
file.close()

# print(data.info())
data = data.drop([0])
data = data.replace('\n','', regex=True)
# print(data.head())

# Locate building coordinates 
# from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3

# geolocator = Nominatim(user_agent="myGeocoder", format_string="%s, Hong Kong", timeout=3)
key = 'AIzaSyDZXhy3wabwyf5q2LqE9V75wHroWi9mQt8'
geolocator = GoogleV3(api_key=key, timeout=3)

# Process Dataset Address and remove excessive content 

fullAddress = []
print(len(data))
for i in range(len(data)):

	singleAddress = data['Address'].iloc[i]
	
	if "BLOCK" in singleAddress:
		textInd = singleAddress.find('BLOCK')

		if textInd < 8:
			truncAddress = singleAddress[textInd+9:]

		truncAddress = truncAddress.replace('NO.', '')

	elif "NO." in singleAddress:
		textInd = singleAddress.find('NO.')
		if textInd < 6:
			truncAddress = singleAddress[textInd+3:]
	else:	

		truncAddress = singleAddress

	fullAddress.append(truncAddress + ' , ' + data['District'].iloc[i] + 
		' , Hong Kong')
	
	
	
	try:
		location = geolocator.geocode(fullAddress[i])
		print(fullAddress[i])
		# print((location.latitude, location.longitude))
		prinit(location)
	except:
		print('Cannot find')

