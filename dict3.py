phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

for name, number in phonebook.items():
    print (name, number)

phonebook['Jake'] = 938273443    
phonebook.pop('Jill')
print(phonebook)
