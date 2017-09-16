#class and objects

class MyClass:

    myVar = "xyz"

    def myFunc(self):
        print('message from function')

myObjX = MyClass()
myObjY = MyClass()

myObjY.myVar = "abc"

print(myObjX.myVar)
print(myObjY.myVar)

myObjX.myFunc()
