# twitter friends list

import urllib.request, urllib.error, urllib.parse
import json
import ssl
import twurl

account_name = input('Enter twitter account: ')
url = twurl.augment('https://api.twitter.com/1.1/friends/list.json',
    {'screen_name':account_name,'count':'5'})
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

# get headers
headers = dict(connection_to_twitter.getheaders())
print('Remaining limit = ', headers['x-rate-limit-remaining'])

for user in js['users']:
    print(user['name'], '@' + user['screen_name'])
    # if 'status' in user:
    #     print(user['status']['text'])
