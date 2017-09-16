def calc(a,b,**option):
    oper = option.get('oper')
    if oper=='add':
        return a + b
    if oper=='sub':
        if option.get('first')=='a':
            return a - b
        else:
            return b - a
    if oper=='mul':
        return a * b
    if oper =='div':
        if option.get('first')=='a':
            return a / b
        else:
            return b / a

print(calc(5,6,oper='sub',first='a'))
