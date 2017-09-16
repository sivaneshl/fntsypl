num = 0
tot = 0
while True:
    sval = input('Enter a anumber:')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
    num = num + 1
    tot = tot + fval
print (tot, num, tot / num)
    
