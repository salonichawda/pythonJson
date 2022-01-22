import json

file='Text.txt'

dic1={}

json_file=open(file)

for line in json_file:
        k,v=line.strip().split(None,1)

        dic1[k]=v.strip()

a=open("myfile8.json","w")

json.dump(dic1, a,indent=6)

a.close()



