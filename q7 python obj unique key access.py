import json

json_file='{"a":  1,"a":  2,"a":  3, "a": 4, "b": 1, "b": 2}'

dic=json.loads(json_file)

dic1={}

for k,v in dic.items():
  
    if k not in dic1:
  
        dic1.update({k:v})

print(dic1)

# my_file=open("myfile7.json",'w')

# json.dump(dic1, my_file,indent=4)

