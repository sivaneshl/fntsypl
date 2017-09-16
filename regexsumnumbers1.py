import re


fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('using default file name to continue')
    fhand = open('regex_sum_42.txt')
    
tot = 0    
for line in fhand:
    num = re.findall('[0-9]+', line)
    if len(num) == 0:
        continue
    else:
        for i in range(len(num)):
            tot = tot + int(num[i])
print(tot)
