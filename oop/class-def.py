# class and objects

class MyClass:
    x = 0

    def myMethod(self):
        self.x = self.x + 1
        print(self.x)

obj = MyClass()

print(type(obj))
print(dir(obj))

obj.myMethod()
obj.myMethod()
obj.myMethod()
