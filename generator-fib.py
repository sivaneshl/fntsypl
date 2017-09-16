# generator-fib.py

def fib():
    b=0
    a=1
    while True:
        a=a+b
        yield a
        b,a=a,b

# for num in fib():
#     print(num)

counter = 0
for n in fib():
    print(n)
    counter += 1
    if counter == 10:
        break
