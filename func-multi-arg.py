# Multiple function arguments

def myfunction(one, two, three):
    print(one)
    print(two)
    print(three)

def myfuncvariable (one, two, *vararg):
    print(one)
    print(two)
    print(list(vararg))
    print(vararg[1])

myfunction("abc", True, 938.9)
myfuncvariable("abc","def", 1,2.142,'three',4,False)
