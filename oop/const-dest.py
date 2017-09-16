# class and objects
# constructors and destructors

class MyClass:
    x = 0

    # constructor
    def __init__(self):
        print('in constructor')

    def myMethod(self):
        self.x = self.x + 1
        print(self.x)

    # destructor
    def __del__(self):
        print('in destructor', self.x)

obj = MyClass()
obj.myMethod()
obj.myMethod()
obj.myMethod()

obj = 72
print(obj)
