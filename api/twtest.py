# twtest.py

import urllib.request, urllib.error, urllib.parse
import twurl
import ssl
import json

print('... calling twitter...')
# url = twurl.augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
#     {'screen_name':'sivaneshl','count':'5'})

hash_tag = input('Enter # : ')
# url = twurl.augment('https://api.twitter.com/1.1/search/tweets.json',
#     {'q':hash_tag,'count':5})
url = twurl.augment('https://api.twitter.com/1.1/search/tweets.json',
    {'q':hash_tag})

print(url)

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# open the url and get the data
connection_to_twitter = urllib.request.urlopen(url,context=ctx)
data_from_twitter = connection_to_twitter.read().decode()
js = json.loads(data_from_twitter)
# print(json.dumps(js,indent=2))

count = 0
statuses = js['statuses']
for status in statuses:
    print(status['user']['screen_name'])
    print('   ', status['text'])
    count = count + 1
print(count)    

# get headers
headers = dict(connection_to_twitter.getheaders())
print(headers['x-rate-limit-remaining'])
