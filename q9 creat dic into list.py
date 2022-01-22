import json

l1=['neelam','programer','24','2400']
l2=['komal','trainer','24','20000']
l3=['anuradha','HR','25','40000']
l4=['Abhishek','manager','29','63000']
l5=['name','designation','age','salary']
dic1={}

dic2={}

dic3={}

dic4={}

dic5={}

for i in range(len(l1)):
    
    dic1.update({l5[i]:l1[i]})
    dic2.update({l5[i]:l2[i]})
    dic3.update({l5[i]:l3[i]})
    dic4.update({l5[i]:l4[i]})

dic5.update({'emp1':dic1,'emp2':dic2,'emp3':dic3,'emp4':dic4})

json_file=open("json_file.json",'w')

json.dump(dic5,json_file,indent=6)

