import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

# ignore ssl certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)

xmldata = urllib.request.urlopen(url, context=ctx).read()
# print(xmldata)
print('Retrieved', len(xmldata), 'characters')

comments = ET.fromstring(xmldata)
countlist = comments.findall('.//count')
cnt = 0
tot = 0
for count in countlist:
    cnt = cnt + 1
    tot = tot + int(count.text)
print ('Count:', cnt)
print ('Sum:', tot)
