import urllib.request, urllib.parse, urllib.error


fhand = urllib.request.urlopen('https://en.wikipedia.org/wiki/Charles_Severance')
for line in fhand:
    print(line.decode().strip())
