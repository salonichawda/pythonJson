import json

dict1={
        "name": "David", 
        "class": "I", 
        "age": 6
    }

my_file=open("myfile2.json",'w')

print(json.dump(dict1,my_file,indent=4))