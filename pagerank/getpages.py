import sqlite3
import ssl
import urllib
import bs4

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# connect to data base pagerank
conn = sqlite3.connect("pagerank.sqlite")
cur = conn.cursor()

# create the necessary tables if not exists
cur.execute('''CREATE TABLE IF NOT EXISTS pages
    (id INTEGER UNIQUE PRIMARY KEY, url TEXT UNIQUE,
    html TEXT, error INTEGER, old_rank REAL, new_rank REAL)''')
cur.execute('''CREATE TABLE IF NOT EXISTS links
    (from_id INTEGER, to_id INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS websites
    (url TEXT UNIQUE)''')

# start with a new url
starturl = input('Enter a new URL or press ENTER to use default URL: ')
# use the default url if the user did not enter any
if (len(starturl) < 1):
    starturl = 'https://en.wikipedia.org/'
# if the url ends with '/' - ignore it
if (starturl.endswith('/')):
    starturl = starturl[:-1]
    website = starturl
# if the url ends with .htm or .html
if (starturl.endswith('.htm') or starturl.endswith('.html')):
    pos = starturl.rfind('/')
    website = starturl[:pos]

# add the website entry
if (len(website) > 1):
    cur.execute('INSERT OR IGNORE INTO websites (url) VALUES (?)', (website,))
    # add this url to the pages table
    cur.execute('INSERT OR IGNORE INTO pages (url, html, new_rank) VALUES (?, NULL, 1.0)', (starturl,))
    conn.commit

cur.execute('SELECT url FROM websites')
for row in cur:
    print(row[0])

cur.execute('SELECT url from pages')
for row in cur:
    print(row[0])    
