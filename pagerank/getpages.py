import sqlite3
import ssl
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# connect to data base pagerank
conn = sqlite3.connect("pagerank.sqlite3")
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
website = starturl
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
    conn.commit()

cur.execute('SELECT url FROM websites')
webs = list()
for row in cur:
    webs.append(str(row[0]))
print(webs)


# # get the number of pages to get
# num_pages = 0
# while True:
#     string_value = input ('Enter number of pages: ')
#     if (len(string_value) < 1):
#         exit()
#     try:
#         num_pages = int(string_value)
#         break
#     except:
#         continue
# # print(num_pages)

for i in range(10):
    # get an unretrieved page from pages
    cur.execute('SELECT id,url FROM pages WHERE html IS NULL AND error IS NULL ORDER BY RANDOM() LIMIT 1')
    try:
        row = cur.fetchone()
        fromid = row[0]
        selectedurl = row[1]
    except:
        print('No unretrieved URLs found. Restart by entering a new URL.')
        exit()
    print('Retrieving URL: ' + selectedurl)

    # delete any links from this selected url - this should never happen
    cur.execute('DELETE FROM links WHERE from_id = ?', (fromid,))

    # open the selected url
    try:
        doc = urllib.request.urlopen(selectedurl, context=ctx)
        html = doc.read()
        # print(len(html))
        # check for errors
        if (doc.getcode() != 200):
            print('Error on page ', doc.getcode())
            cur.execute('UPDATE pages SET error = ? WHERE url = ?',(doc.getcode(), selectedurl))
            continue
        if (doc.info().get_content_type() != 'text/html'):
            print('Ignore non text/html page')
            cur.execute('DELETE FROM pages WHERE url = ?', (selectedurl,))
            conn.commit()
            continue
    except KeyboardInterrupt:
        print('Program interrupted by user...')
        break
    except:
        print('Unable to retireve page')
        cur.execute('UPDATE pages SET error = -1 WHERE url = ?',(selectedurl,))
        conn.commit()
        continue

    # update the html to the url in pages
    cur.execute('UPDATE pages SET html = ? WHERE url = ?', (memoryview(html), selectedurl))
    conn.commit()

    # valid page - parse using bs4
    # print('Parsing page: ', selectedurl)
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    newpages = 0
    for tag in tags:
        href = tag.get('href', None)
        if (href is None):
            continue
        # print(href)
        # join relative urls
        if (len((urllib.parse.urlparse(href).scheme)) < 1):
            href = urllib.parse.urljoin(selectedurl, href)
            # print("JOIN", href)
        # ignore images
        if (href.lower().endswith('.png') or href.lower().endswith('.jpg') or href.lower().endswith('.gif')):
            continue
        # ignore urls after #
        pos = href.find('#')
        if (pos > 1):
            href = href[:pos]
        # ignore / at the end of the url
        if (href.endswith('/')):
            href = href[:-1]
        # check for blank urls
        if (len(href) < 1):
            continue

        # check if the parsed url is in the same website
        sameweb = False
        for web in webs:
            if (href.startswith(web)):
                sameweb = True
                # print(sameweb)
                break
        if sameweb == False:
            # print(sameweb)
            continue
        # print('add url')

        print(href)

        # add this new page to pages
        cur.execute('INSERT OR IGNORE INTO pages (url, html, new_rank) VALUES (?, NULL, 1.0)', (href,))
        conn.commit()
        newpages = newpages + 1

        # get the id of the newly added page
        cur.execute('SELECT id FROM pages WHERE url = ?', (href,))
        try:
            toid = cur.fetchone()[0]
        except:
            print('Could not get id')
            continue

        # add to links
        cur.execute('INSERT OR IGNORE INTO links (from_id, to_id) VALUES (?,?)', (fromid, toid))
        conn.commit()

    # stop after retrieving 1 url
    # break

print(newpages)
# print(html)

cur.close()
