import sqlite3

# connect to data base pagerank
conn = sqlite3.connect("pagerank.sqlite3")
cur = conn.cursor()

# find the pages that have external links
cur.execute('SELECT DISTINCT from_id FROM links')
fromids = list()
for row in cur:
    fromids.append(row[0])
# print(fromids)

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

# print(toids)
# print(links)

prevranks = dict()
for fromnode in fromids:
    cur.execute('SELECT new_rank FROM pages WHERE id = ?', (fromnode,))
    # print(cur.fetchone()[0])
    prevranks[fromnode] = cur.fetchone()[0]
# print(pageranks)

inum = 1
snum = input('Enter number of iterations: ')
if (len(snum) > 0):
    inum = int(snum)

for i in range(inum):
    # create a nextrank dict
    nextranks = dict()
    total = 0.0
    for (fromnode, oldrank) in list(prevranks.items()):
        # add sum of old ranks to get total
        total = total + oldrank
        nextranks[fromnode] = 0.0

    # get the outbound links for each from link
    for (fromnode, oldrank) in list(prevranks.items()):
        # create a list of outbound ids from each from node
        outids = list()
        for (fromid, toid) in links:
            if (fromid != fromnode):
                continue
            if (toid not in toids):
                continue
            outids.append(toid)
        if (len(outids) < 1):
            continue
        distributerank = oldrank / len(outids)

        # distribute the rank of the from node to all its to nodes
        for tonode in outids:
            nextranks[tonode] = nextranks[tonode] + distributerank

    # print(prevranks)
    # print(nextranks)

    newtotal = 0.0
    for (node, newrank) in list(nextranks.items()):
        newtotal = newtotal + newrank
    evap = (total - newtotal) / len(nextranks)

    for node in nextranks:
        nextranks[node] = nextranks[node] + evap

    print(prevranks)
    print(nextranks)

    prevranks = nextranks

# set the old rank and new rank in pages
cur.execute('UPDATE pages SET old_rank = new_rank')
for (id, newrank) in list(nextranks.items()):
    cur.execute('UPDATE pages SET new_rank = ? WHERE id = ?', (newrank, id))
conn.commit()
cur.close()    
