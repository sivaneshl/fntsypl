# serialization json

import json

# salaries is a dict
salaries = {"Alfred":300,"Jane":400}
# convert salaries dict to json
#json.loads takes string, not dict
salaries_string = '{"Alfred":300,"Jane":400}'
salaries_json = json.loads(salaries_string)
print(salaries_json, type(salaries_json))
salaries_string = json.dumps(salaries_json)
print(salaries_string, type(salaries_string))
