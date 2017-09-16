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

tags = soupobj('span')
tot = 0
cnt = 0
num = 0
for tag in tags:
    try:
        num = int(tag.contents[0])
    except:
        continue
    tot = tot + num
    cnt = cnt + 1
print('Count', cnt)
print('Sum', tot)
    
