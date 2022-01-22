import json

dic1={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}

k=(input('which item you want:'))

v=int(input('enter the number of items:'))

for i in dic1:

    for j in dic1[i]:

        if int(dic1[i][j])>=v:

            if j==k:

                a=int(dic1[i][j])-v

                dic1[i][j]=str(a)

my_file=open("file.json",'w')

json.dump(dic1, my_file,indent=6)

b=open("file.json","r")

c=b.read()

print(c)

b.close()






# import json

# import os

# file=os.path.exists("Login_system.json")

# if file===str(input('enter'))

# if 'ly' in a:

#     print(a+'ing')

# elif 'ing' in a:

#     print(a+'ly')

# else:

#     print(a+'ly'+'ing ')

# False:

#     choose=input('choose Signup or Login?:')

#     if choose=='signup':

#         username=input('enter your name:')

#         phoneNo=int(input('enter your phone number:'))

#         age=int(input('enter your age:'))

#         description=input('enter your description:')

#         password=input('enter your password:')

#         confirmpass=input('confirm your password:')

#         list1=[]

#         dic1={'Username':username,'PhoneNo':phoneNo,'Age':age,'Description':description,'Password':password}

#         list1.append(dic1)

#         if password==confirmpass:

#             print('Registration successfuly')

#             my_file=open("Login_system.json",'w')

#             json.dump(list1,my_file,indent=6)

#         else:

#             print('Registration failed! please confirm your password correct')
#     else:
#         print('you shuold signup first')

# elif file==True:

#     choose=input('choose Signup or Login?:')

#     if choose=='signup':
    
#         username=input('enter your name:')

#         phoneNo=int(input('enter your phone number:'))

#         age=int(input('enter your age:'))

#         description=input('enter your description:')

#         password=input('enter your password:')

#         confirmpass=input('confirm your password:')

#         dic1={'Username':username,'PhoneNo':phoneNo,'Age':age,'Description':description,'Password':password}

#         a=open("Login_system.json",'r')

#         list1=json.load(a)

#         list1.append(dic1)

#         if password==confirmpass:

#             print('Registration successfuly')

#             my_file=open("Login_system.json",'w')

#             json.dump(list1,my_file,indent=6)

#         else:

#             print('Registration failed! please confirm your password correct')

#     elif choose=='login':

#         username=input('enter your name:')

#         password=input('enter your password:')

#         my_file=open("Login_system.json",'r')

#         a=json.load(my_file)

#         def login_or_not(username,password,a):

#             for i in a:
                        
#                 if i['Username']==username and i['Password']==password:
                            
#                     data = i

#             return data      

#         Data=login_or_not(username, password,a)
        
#         if Data:

#             print(Data)
            
#             print('login successfuly....')

#         else:

#             print('login failed! please enter your correct info....')

# else:

#     print('incorrect')





