import json
import sqlite3

conn = sqlite3.connect('pagerank.sqlite3')
cur = conn.cursor()

cur.execute('''SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url
    FROM pages JOIN links ON pages.id = links.to_id
    WHERE html IS NOT NULL AND error IS NULL
    GROUP BY id ORDER BY id, inbound''')

fhand = open('pagerank/pagerank.js','w')

nodes = list()
maxrank = None
minrank = None
for row in cur:
    nodes.append(row)
    rank = row[2]
    if maxrank == None or maxrank < rank:
        maxrank = rank
    if minrank == None or minrank > rank:
        minrank = rank


fhand.write('pagerankJson = {"nodes":[\n')
count = 0
map = dict()
ranks = dict()
for row in nodes:
    rank = row[2]
    rank = 19 * ((rank - minrank) / (maxrank - minrank))
    if (count > 0):
        fhand.write(',\n')
    fhand.write('{"weight":' + str(row[0]) + ',"rank":' + str(row[2]) + ', "id":' + str(row[3]) + ', "url":"' +  row[4] + '"}')
    map[row[3]] = count
    ranks[row[3]] = rank
    count = count + 1
fhand.write('],\n')

cur.execute('''SELECT DISTINCT from_id, to_id FROM links''')
fhand.write('"links":[\n')
count = 0
for row in cur:
    if row[0] not in map or row[1] not in map:
        continue
    if count > 0:
        fhand.write(',\n')
    rank = ranks[row[0]]
    srank = 19 * ( (rank - minrank) / (maxrank - minrank) )
    fhand.write('{"source":' + str(map[row[0]]) + ',"target":' + str(map[row[1]]) + ',"value":' + str(srank) + '}')
    count = count + 1
fhand.write(']};')

fhand.close()
cur.close()
