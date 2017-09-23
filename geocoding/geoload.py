import json
import urllib.request, urllib.parse, urllib.error
import sqlite3

conn = sqlite3.connect('geodata.sqlite3')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS geodata (univ_name TEXT UNIQUE, univ_addr TEXT, univ_lat TEXT, univ_lng TEXT)')

service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'
fhand = open("where.data")
for line in fhand:

    line = line.strip()
    print(line)

    cur.execute('SELECT * FROM geodata WHERE univ_name = ? LIMIT 1',(line,))
    try:
        line = cur.fetchone()[0]
        print('Found in database')
        continue
    except:
        print('except')
        pass

    # encode with the input address
    url = service_url + urllib.parse.urlencode({'address':line})
    print('Retrieving:', url)

    # use urlopen to hit the google api
    url_handle = urllib.request.urlopen(url)
    output_data = url_handle.read().decode()

    # convert to json
    try:
        js = json.loads(output_data)
    except:
        js = None
        print('Failure to retrieve data from google')
        continue

    # parse the dict and check if the status is OK
    if not js or 'status'not in js or js['status'] != 'OK':
        print('Failure to retrieve data from google')
        print(js)
        continue

    # headers = dict(url_handle.getheaders())
    # print(headers)

    # retrieve formatted address
    formatted_address = (js['results'][0]['formatted_address'])

    # retrieve lat and long
    location_latitude = js['results'][0]['geometry']['location']['lat']
    location_longitude = js['results'][0]['geometry']['location']['lng']

    print (formatted_address, location_latitude, location_longitude)

    cur.execute('INSERT INTO geodata (univ_name, univ_addr, univ_lat, univ_lng) VALUES (?, ?, ?, ?)', (line, formatted_address, location_latitude, location_longitude))
    conn.commit()

cur.close()
conn.close()
