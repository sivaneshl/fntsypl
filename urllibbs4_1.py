import ssl
import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup


# ignore ssl certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input ('Enter url - ')
cnt = int(input ('Enter times - '))
pos = int(input ('Enter position - '))


i = 0
print('Retrieving:', url)
for i in range(cnt):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = (tags[pos - 1])
    url = (tag.get('href', None))
    print('Retrieving:', url)
    if len(tag.contents[0]) > 0:
        val = tag.contents[0]
print(val)

