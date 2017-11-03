import sqlite3

# connect to data base pagerank
conn = sqlite3.connect("pagerank.sqlite3")
cur = conn.cursor()

# find the pages that have external links
cur.execute('SELECT DISTINCT from_id FROM links')
fromids = list()
for row in cur:
    fromids.append(row[0])
print(fromids)

toids = list()
links = list()
# get the distint links and contruct the links dict
cur.execute('SELECT DISTINCT from_id, to_id FROM links')
for row in cur:
    fromid = row[0]
    toid = row[1]
    # ignore any links pointing to the same page
    if (fromid == toid):
        continue
    # ignore if the link is not in our list - this is only a precaution
    if (fromid not in fromids):
        continue
    # ignore if the toid page is not retireved yet or not in our scope
    if (toid not in fromids):
        continue
    # add this link to the links dict
    links.append(row)
    #construct the toids list
    if (toid not in toids):
        toids.append(toid)

print(toids)
print(links)
