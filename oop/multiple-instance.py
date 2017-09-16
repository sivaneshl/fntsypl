# multiple instances for a class

class Person:
    x = 0
    name = ""

    def __init__(self, name):
        self.name = name
        print(self.name, 'constructed')

    def incrementPerson(self):
        self.x = self.x + 1
        print(self.name, self.x)

r = Person('Rooney')
r.incrementPerson()
g = Person('Giggs')
g.incrementPerson()
r.incrementPerson()
