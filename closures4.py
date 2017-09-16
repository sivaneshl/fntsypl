def multiplier_of(multiplier):
    def multiply_func(number):
        print(number * multiplier)
    return multiply_func

multiplywith5 = multiplier_of(5)
multiplywith5(9)

multiplywith4 = multiplier_of(4)
multiplywith4(9)
