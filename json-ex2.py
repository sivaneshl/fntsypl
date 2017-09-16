import json
import urllib.parse, urllib.request, urllib.error

service_url = 'http://py4e-data.dr-chuck.net/geojson?'
input_address = input('Enter Location: ')
url = service_url + urllib.parse.urlencode({'address':input_address})
url_handle = urllib.request.urlopen(url)
output_data = url_handle.read().decode()
js = json.loads(output_data)

if not js or 'status'not in js or js['status'] != 'OK':
    print('Failure to retrieve data from google')
    print(js)
    exit()

print(js['results'][0]['place_id'])
