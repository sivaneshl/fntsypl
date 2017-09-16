mynum = input('Enter a number:')
try:
    mynum = int(mynum)
except:
    mynum = -1

if mynum > 0 :
    print('Number')
else:
    print('Not a number')
    
    
