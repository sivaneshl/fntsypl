import sqlite3
import ssl
import urllib.parse, urllib.request, urllib.error
import re
import dateutil.parser

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# create/connect the database
conn = sqlite3.connect('mailbox/mailbox.sqlite3')
cur = conn.cursor()

# create table messages
cur.execute('''CREATE TABLE IF NOT EXISTS messages
    (id INTEGER UNIQUE, email TEXT, sent_at TEXT,
    subject TEXT, headers TEXT, body TEXT)''')

# base url for api
baseurl = "http://mbox.dr-chuck.net/sakai.devel/"

# get the last retrieved message number
start = None
cur.execute('SELECT MAX(id) FROM messages')
try:
    row = cur.fetchone()
    if row is None:
        start = 0
    else:
        start = row[0]
except:
    start = 0
if start is None:
    start = 0

# get how many messages to get
howmany = 0
while True:
    string_value = input ('How many messages? ')
    if (len(string_value) < 1):
        exit()
    try:
        howmany = int(string_value)
        break
    except:
        continue
# print(howmany)

i = 0
fail = 0
count = 0
while i in range(howmany):
    start = start + 1
    # print(start)
    i = i + 1
    url = baseurl + str(start) + '/' + str(start + 1)
    print(url)

    doc = None
    text = None
    try:
        doc = urllib.request.urlopen(url, None, 30, context=ctx)
        text = doc.read().decode()
        if (doc.getcode() != 200):
            print('Error code = ', doc.getcode(), url)
            break
    except KeyboardInterrupt:
        print('Interupted by user...')
        break
    except Exception as e:
        print('Unable to retrieve or parse page', url)
        print('Error ', e)
        fail = fail + 1
        if fail > 5:
            break
        continue

    # increment counter - successfully retrieved pages
    count = count + 1
    # print(text)

    # Find the from line
    if not text.startswith('From '):
        print('Did not start with From ')
        fail = fail + 1
        if fail > 5:
            break
        continue

    # get header and body
    pos = text.find('\n\n')
    if (pos > 0):
        headertext = text[:pos]
        bodytext = text[pos+2:]
    else:
        print('Could not find break between header and body')
        fail = fail + 1
        if fail > 5:
            break
        continue

    # get email address
    emailid = None
    x = re.findall('\nFrom: .*<(\S+@\S+)>\n', headertext)
    # print(x, len(x))
    if (len(x) != 1):
        x = re.findall('\nFrom: (\S+@\S+)\n', headertext)
    emailid = x[0].strip().lower()
    emailid = emailid.replace("<","")
    # print(emailid)

    # get date
    sentdate = None
    x = re.findall('\nDate: .*, (.*)\n', headertext)
    # print(x)
    if (len(x) == 1):
        # print(x[0][:26])
        try:
            sentdate = dateutil.parser.parse(x[0][:26]).isoformat()
        except:
            print('Unable to get/parse date')
            fail = fail + 1
            if fail > 5:
                break
            continue

    # get the subject
    subject = None
    x = re.findall('\nSubject: (.*)\n', headertext)
    if (len(x) == 1):
        subject =  x[0].strip().lower()

    fail = 0
    print(emailid, sentdate, subject)
    cur.execute('''INSERT OR IGNORE INTO messages
        (id, email, sent_at, subject, headers, body)VALUES(?,?,?,?,?,?)''',
        (start, emailid, sentdate, subject, headertext, bodytext))
    if count % 50 == 0:
        conn.commit()
    if count % 100 == 0:
        time.sleep(1)

conn.commit()
cur.close()
