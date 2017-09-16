# google geocoding api

import urllib.request, urllib.parse, urllib.error
import json

# google goecoding service url
# format: http://maps.googleapis.com/maps/api/geocode/json?address=%22manapakkam%22
service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'
# get the location from user
input_address = input('Enter Location: ')
if len(input_address) < 1:
    exit()

# encode with the input address
url = service_url + urllib.parse.urlencode({'address':input_address})
# print("Retrieving ...", url)

# use urlopen to hit the google api
url_handle = urllib.request.urlopen(url)
output_data = url_handle.read().decode()
# print('Retrieved', len(output_data), 'characters')

# convert the data to a json / dictionary
try:
    js = json.loads(output_data)
except:
    js = None
    print('Failure to retrieve data from google')
    exit()

# parse the dict and check if the status is OK
if not js or 'status'not in js or js['status'] != 'OK':
    print('Failure to retrieve data from google')
    print(js)
    exit()
# dumps used to print dictionary
print(json.dumps(js, indent=4))

# retrieve formatted address
print(js['results'][0]['formatted_address'])

# retrieve country name from address_components
address_components = js['results'][0]['address_components']
for i in range(len(address_components)):
    for geo_type in (address_components[i]['types']):
        if geo_type == 'country':
            geo_country = (address_components[i]['long_name'])

    #geo_country = [(address_components[i]['long_name']) for geo_type in address_components[i]['types'] if geo_type == 'country']
    #using list comprehension will over-write the geo_country list again for each i
print(geo_country)

# retrieve lat and long
location = js['results'][0]['geometry']['location']
print(location['lat'],location['lng'])
