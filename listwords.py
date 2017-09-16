fname = input("Enter file name:")

try:
    fhand = open(fname)
except:
    print("Enter a valid file name!!!")
    quit()

newlist = list()
for line in fhand:
    linewords = line.split()
    for i in range(len(linewords)):
        if linewords[i] in newlist:
            continue
        newlist.append(linewords[i])
newlist.sort()
print (newlist)
