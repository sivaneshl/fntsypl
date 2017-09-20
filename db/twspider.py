import urllib
import json
import sqlite3
import sys
sys.path.insert(0,'/home/sivaneshl/python/py3/pyhton-tutorials/api')
import twurl # relative path of twurl.py added to sys.path & __init__.py added to that folder

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS twfriends (name TEXT, retrieved INTEGER, friends INTEGER)')

while True:
    account_name = input('Enter Account Name: ')

    if (account_name == 'quit'):
        break

    if len(account_name) < 1:
        cur.execute('SELECT name from twfriends WHERE retrieved = 0 LIMIT 1')
        try:
            account_name = cur.fetchone()[0]
        except:
            print('No unretrieved Twitter accounts found')
            continue

    cur.execute('INSERT INTO twfriends (name, retrieved, friends) VALUES (?, ?, ?)', (account_name, 1, 0))

    url = twurl.augment('https://api.twitter.com/1.1/friends/list.json',
        {'screen_name':account_name,'count':'5'})

    connection_to_twitter = urllib.request.urlopen(url)
    data_from_twitter = connection_to_twitter.read().decode()
    js = json.loads(data_from_twitter)

    headers = dict(connection_to_twitter.getheaders())
    print('Attempts Remaining', headers['x-rate-limit-remaining'])

    cur.execute('UPDATE twfriends SET retrieved = 1 WHERE name = "' + account_name + '"')

    for user in js['users']:
        friend = user['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM twfriends WHERE name = ? LIMIT 1', (friend,))
        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE twfriends SET count = ? WHERE name = ?', (count + 1, friend))
        except:
            cur.execute('INSERT INTO twfriends (name, retrieved, friends) VALUES (?, ?, ?)', (friend, 0, 1))

    conn.commit()

cur.close()
