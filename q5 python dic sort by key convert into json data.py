# import json

# dic1={
#         '4': 5, 
#         '6': 7, 
#         '1': 3, 
#         '2': 4
#     }

# dic2=dict(sorted(dic1.items()))

# # print(dic2)

# my_file=open("myfile5.json",'w')

# json.dump(dic2,my_file,indent=4)


a=[2,4,5,6,7,8]

d={}

for i in range(len(a)):

    for j in a:

        d.update({j:j})

print(d)