fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)

sender = dict()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        sender[words[1]] = sender.get(words[1], 0) + 1
    else:
        continue

bigname = None
bigcount = None
for k, v in sender.items():
    if bigcount == None or v > bigcount:
        bigname = k
        bigcount = v
        
print(bigname, bigcount)    	
