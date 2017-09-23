import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS movies (dummy INTEGER, id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)')

movie_name = input('Enter Movie Name: ')

cur.execute('INSERT INTO movies (dummy, name) VALUES ("XXX",?)', (movie_name,))
conn.commit()
# print(cur.lastrowid, cur.rowcount)
movie_id = 0
movie_name = ""
cur.execute('SELECT * FROM movies LIMIT 1')
try:
    row = cur.fetchone()
    print(row)
    movie_id = row[1]
    movie_name = row[2]
except:
    print('fail')

print(movie_id, movie_name)
