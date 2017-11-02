import urllib
import json
import sqlite3
import sys
# sys.path.insert(0,'C:/python_learning/api')
sys.path.append("../api")
import twurl # relative path of twurl.py added to sys.path & __init__.py added to that folder

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, name TEXT UNIQUE, retrieved INTEGER)')
cur.execute('CREATE TABLE IF NOT EXISTS follows (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))')

while True:
    acct = input('Enter Twitter Account Name: ')

    if acct == 'quit':
        break

    if len(acct) < 1:
        cur.execute('SELECT id, name FROM people WHERE retrieved = 0 LIMIT 1')
        try:
            (id, name) = cur.fetchone()
        except:
            print('No more unretrieved Twitter accounts. Please enter a Twitter account!!!')
            continue

    else:
        cur.execute('SELECT id, retrieved FROM people WHERE name = ? LIMIT 1', (acct,))
        try:
            (id, rtrvd) = cur.fetchone()
            if rtrvd == 1:
                print('Account already retrieved')
                continue
        except:
            cur.execute('INSERT OR IGNORE INTO people (name, retrieved) VALUES (?, 0)', (acct,))
            conn.commit()
            if cur.rowcount != 1:
                print('Error while inserting: ', acct)
                continue
            id = cur.lastrowid
            rtrvd = 0

    url = twurl.augment('https://api.twitter.com/1.1/friends/list.json',
        {'screen_name':acct,'count':'5'})
    connection_to_twitter = urllib.request.urlopen(url)
    data_from_twitter = connection_to_twitter.read().decode()
    js = json.loads(data_from_twitter)

    headers = dict(connection_to_twitter.getheaders())
    print('Remaining Attempts Left:', headers['x-rate-limit-remaining'])

    cur.execute('UPDATE people SET retrieved = 1 WHERE name = ?', (acct,))
    conn.commit()

    users = js['users']
    for user in users:
        friend = user['screen_name']
        print(friend)

        cur.execute('SELECT id FROM people WHERE name = ? LIMIT 1', (friend,))
        try:
            friend_id = cur.fetchone()[0]
        except:
            cur.execute('INSERT OR IGNORE INTO people (name, retrieved) VALUES (?, 0)', (friend,))
            conn.commit()
            if cur.rowcount != 1:
                print('Error while inserting: ', acct)
                continue
            friend_id = cur.lastrowid

        cur.execute('INSERT OR IGNORE INTO follows (from_id, to_id) VALUES (?, ?)', (id, friend_id))

    conn.commit()

cur.close()
conn.close()
