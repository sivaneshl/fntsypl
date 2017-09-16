# json with list

import json

data = '''[
    {
        "name":"Wayne Rooney",
        "team":"Manchester United",
        "goals":48
    },
    {
        "name":"Cristiano Ronaldo",
        "team":"Real Madrid",
        "goals":56
    }
]'''

data_list = json.loads(data)
print(data_list)
print(type(data_list), len(data_list))
for player in data_list:
    print(player["name"],player["team"],player["goals"])
