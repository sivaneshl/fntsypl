mydict = dict()
mydict["name"] = "siva"
mydict["age"] = 30
mydict["job"] = "Engineer"
print(mydict)
mydict['age'] = 32
print(mydict)

print('job' in mydict)
print('tech' in mydict)

for key in mydict:
    print(key, mydict[key])

print(list(mydict))
print(mydict.keys())
print(mydict.values())
print(mydict.items())

for k, v in mydict.items():
    print(k, v)
