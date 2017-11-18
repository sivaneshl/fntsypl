import sqlite3

conn = sqlite3.connect('index.sqlite3')
cur = conn.cursor()

senders = dict()
cur.execute('SELECT id, sender FROM senders')
for row in cur:
    senders[row[0]] = row[1]

messages = dict()
cur.execute('SELECT id, guid, sender_id, subject_id, sent_at FROM messages')
for row in cur:
    messages[row[0]] = (row[1], row[2], row[3], row[4])

sendorgs = dict()
for (messageid, message) in list(messages.items()):
    sender = message[1]
    pieces = (senders[sender]).split("@")
    if len(pieces) != 2:
        continue
    org = pieces[1]
    sendorgs[org] = sendorgs.get(org,0) + 1

orgs = sorted(sendorgs, key=sendorgs.get, reverse=True)
orgs = orgs[:10]
print('Top 10 Organizations')
print(orgs)

counts = dict()
months = list()
for (messageid, message) in list(messages.items()):
    sender = message[1]
    pieces = senders[sender].split("@")
    if len(pieces) != 2:
        continue
    org = pieces[1]
    if org not in orgs:
        continue
    month = message[3][:7]
    if month not in months:
        months.append(month)
    key = (month,org)
    counts[key] = counts.get(key,0) + 1

months.sort()
# print(counts)

fhand = open('mailline.js','w')
fhand.write("mailline = [ [ 'Year'")
for org in orgs:
    fhand.write(",'"+org+"'")
fhand.write("]")

for month in months:
    fhand.write(",\n['"+month+"'")
    for org in orgs:
        key = (month, org)
        val = counts.get(key,0)
        fhand.write(","+str(val))
    fhand.write("]")
fhand.write("\n];\n")
fhand.close()

cur.close()
