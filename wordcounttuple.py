# get file name
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('Enter a valid file name!!!')
    quit()
    
wordcount = dict()    
# loop through each line in the file
for line in fhand:
    # split all the words in the line
    words = line.split()
    for word in words:
        # construct a dict with all the words and their count
        wordcount[word] = wordcount.get(word, 0) + 1
        
wordlist = list()
# to sort by value (not key) we need to create a temp list with value, key (reverse)
for k, v in wordcount.items():
    # tuple with v,k
    wordtup = (v, k)
    # temp list of tuples
    wordlist.append(wordtup)

# sort the list descending order
wordlist = sorted(wordlist, reverse=True)
# slice the sorted list for first 10 items and display the key, value
for v, k in wordlist[:10]:
    print(k, v)
