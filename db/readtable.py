# readtable.py

import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

cur.execute('SELECT * FROM twfriends')
for row in cur:
    print(row)

cur.execute('SELECT COUNT(*) FROM twfriends')
count = cur.fetchone()[0]
print(count)
