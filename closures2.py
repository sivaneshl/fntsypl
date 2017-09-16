# closures with nonlocal keyword

def print_msg(number):
    def printer():
        nonlocal number # with nonlocal , the value of number gets changed 
        number = 3
        print(number)

    printer()
    print(number)

print_msg(9)
