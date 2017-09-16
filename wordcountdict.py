fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('Enter a valid file name!!!')
    quit()
    
counts = dict()    
    
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
bigword = None
bigcount = None
for k, v in counts.items():
    if bigcount == None or v > bigcount:
        bigcount = v
        bigword = k
        
print(bigword, bigcount)
    
