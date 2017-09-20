import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

acct = input('Enter Twitter Account: ')
cur.execute('SELECT id FROM people WHERE name = ? AND retrieved = 1', (acct,))
try:
    id = cur.fetchone()[0]
except:
    print('Account Not Retrieved Yet')
    quit()

cur.execute('SELECT * FROM follows JOIN people ON follows.to_id = people.id AND follows.from_id = ?', (id,))
print(cur.rowcount)
for row in cur:
    print(row)

cur.close()
conn.close()
