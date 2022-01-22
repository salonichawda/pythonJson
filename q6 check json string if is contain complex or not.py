import json

json_str='{"complex":5+0j}'

a=json.loads(json_str)

print(a)


# complex does not exist in json file