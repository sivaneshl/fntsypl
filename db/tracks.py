import sqlite3

# The connect operation makes a “connection” to the database stored in the file
# music.sqlite3 in the current directory. If the file does not exist, it will be created.
conn = sqlite3.connect('music.sqlite3')

# A cursor is like a file handle that we can use to perform operations on the data
# stored in the database. Calling cursor() is very similar conceptually to calling
# open() when dealing with text files.
cur = conn.cursor()

# Once we have the cursor, we can begin to execute commands on the contents of
# the database using the execute() method
cur.execute('DROP TABLE IF EXISTS tracks')
cur.execute('CREATE TABLE tracks (title TEXT, plays INTEGER)')

# insert data into the table
cur.execute('INSERT INTO tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
cur.execute('INSERT INTO tracks (title, plays) VALUES (?, ?)', ('My Way', 15))

# commit data
conn.commit()

# Using SELECT statement to retrieve the contents of a TABLE
cur.execute('SELECT * FROM tracks')
# We need use the cursor to print the rows
for row in cur:
    print (row)

# To get only one row - we can use the fetchone() function
cur.execute('SELECT * FROM tracks')
first_row = cur.fetchone()
print(first_row)
# fetchone() will return a tuple. We can use [] to get the fields
print(first_row[0], first_row[1])

# Or use fetchone() to get a particular field in a variable
cur.execute('SELECT title FROM tracks')
first_title = cur.fetchone()
print(first_title)

# cur.execute('DELETE FROM tracks WHERE plays < 100')
# conn.commit()

cur.close()
