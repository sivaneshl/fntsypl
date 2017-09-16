# json
import json

data = ''' {
    "name":"John",
    "age":30,
    "cars": {
        "car1":"Ford",
        "car2":"BMW",
        "car3":"Fiat"
    }
 }'''

data_dict = json.loads(data)
print(data_dict)
print(type(data_dict))
print(len(data_dict))
print(data_dict["name"], data_dict["age"])
print(data_dict["cars"])
print(data_dict["cars"]["car2"])
