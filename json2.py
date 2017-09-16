import json
json_string = '{"x":1,"y":2}'
jsonobj=(json.loads(json_string))
print(jsonobj,type(jsonobj))
