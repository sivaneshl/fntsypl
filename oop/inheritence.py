# inheritence

# base class
class Person:
    x = 0
    name = ""

    def __init__(self, name):
        self.name = name
        print(self.name, "of", type(self), "constructed")

    def incrementPerson(self):
        self.x = self.x + 1
        print(self.name, self.x)

# sub-class of Person
class Player(Person):
    goals = 0

    def addGoals(self,i):
        self.goals = self.goals + i
        self.incrementPerson()
        print(self.name, 'goals:-', self.goals)

r = Person('Rooney')
r.incrementPerson()

s = Player('Silva')
s.addGoals(3)
