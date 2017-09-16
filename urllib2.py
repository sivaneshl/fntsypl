import ssl
import urllib.request 

from bs4 import BeautifulSoup


# ignore ssl certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input ('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()

soupobj = BeautifulSoup(html, 'html.parser')

tags = soupobj('a')
for tag in tags:
    print(tag.get('href', None))
    if(len(tag.contents) > 0):
        print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
