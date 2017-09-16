import json
import urllib.request, urllib.error, urllib.parse

url = input('Enter url: ')
url_handle = urllib.request.urlopen(url)
js_data = url_handle.read().decode()
js = json.loads(js_data)
tot = 0
for comment in js['comments']:
    tot = tot + int(comment['count'])
print(tot)
