import sqlite3

conn = sqlite3.connect('geodata.sqlite3')
cur = conn.cursor()

cur.execute('SELECT * FROM geodata')
fhand = open("where.js","w")
fhand.write("myData = [\n")

count = 0
for row in cur:
    count = count + 1
    if count > 1:
        fhand.write(",\n")
    location = row[1].replace("'","")
    fhand.write("[" + str(row[2]) + "," + str(row[3]) + ", '" + location + "']")

fhand.write("\n]\n")

cur.close()
conn.close()
