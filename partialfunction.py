from functools import partial

def multiply(x,y):
    print(x,y)
    return x * y

dbl = partial(multiply,2)
# 2 will replace x in multiply
# 4 will replace y in multiply only when dbl() is called
print(dbl(4))


###############################
def func(u,v,w,x):
    print(u,v,w,x)
    return u*4 + v*3 + w*2 + x

callpartial = partial(func,2,3,4)
print(callpartial(35))
