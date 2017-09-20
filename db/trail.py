import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS movies (id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)')

movie_name = input('Enter Movie Name: ')

cur.execute('INSERT INTO movies (name) VALUES (?)', (movie_name,))
conn.commit()
print(cur.lastrowid, cur.rowcount)
