# generators.py

import random

def lotteryfunc():
    # returns a random number between 1 and 50 - 6 times
    for i in range(6):
        yield random.randint(1,50)

for randomnumber in lotteryfunc():
    print(randomnumber)
