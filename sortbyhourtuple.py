# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# get file name and open it
fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)

hourdict = dict()
# loop through each line
for line in fhand:
    if line.startswith('From '):
        # fromline = line.split()
        # timepart = fromline[5].split(':')
        # hour = timepart[0]
        # print(timepart,hour)
        hour = line.split()[5].split(':')[0]
        hourdict[hour] = hourdict.get(hour, 0) + 1
    else:
        continue
    
# convert to list of tuples    
hourlist = list()    
for k, v in hourdict.items():
    newtuple = (k, v)
    hourlist.append(newtuple)
    
# sort hourlist in reverse order
hourlist = sorted(hourlist)

for k, v in hourlist:
    print(k, v)
    
