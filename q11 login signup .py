import json

import os

import re

file=os.path.exists("Login_system.json")

if file==False:

    choose=input('choose Signup or Login?: ')

    if choose=='signup':

        username=input('enter your name: ')

        phoneNo=int(input('enter your phone number: '))

        age=int(input('enter your age:'))

        description=input('enter your description: ')

        hobby=input('enter your hobby: ')

        password=input('enter your password: ')

        pattern=("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])");

        for i in password:
            
                if len(password)>=6 and len(password)<=12:

                    if not re.search('[A-Z]', password):

                        print('please include a upper case letter')

                        break

                    if not re.search('[a-z]', password):

                        print('please include a lower case letter')

                        break

                    if not re.search('[0-9]', password):

                        print('please include a digit')

                        break

                    if not re.search('[!@#\$%\^&\*]', password):
                    
                        print('please include a special charector')

                        break
                        

                    else:

                            print('strong pass')

                            break

                else:
                    print('wrong length')

                    password=input('enter your  password again : ')

                    pattern=("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])");

                    for i in password:
                    
                        if len(password)>=6 and len(password)<=12:

                            if not re.search('[A-Z]', password):

                                print('please include a upper case letter')

                                break

                            if not re.search('[a-z]', password):

                                print('please include a lower case letter')

                                break

                            if not re.search('[0-9]', password):

                                print('please include a digit')

                                break

                            if not re.search('[!@#\$%\^&\*]', password):
                            
                                print('please include a special charector')

                                break
                                

                            else:

                                    print('strong pass')

                                    break

                        else:
                            print('wrong length')
                            
                            break
                

        confirmpass=input('confirm your password: ')

        list1=[]

        dic1={'Username':username,'PhoneNo':phoneNo,'Age':age,'Description':description,'Hobby':hobby,'Password':password}

        list1.append(dic1)

        if password==confirmpass:

            print('Registration successfuly')

            my_file=open("Login_system.json",'w')

            json.dump(list1,my_file,indent=6)

        else:

            print('Registration failed! please confirm your password correct')
    else:
        print('you shuold signup first')

elif file==True:

    choose=input('choose Signup or Login?: ')

    if choose=='signup':
    
        username=input('enter your name: ')

        phoneNo=int(input('enter your phone number: '))

        age=int(input('enter your age: '))

        description=input('enter your description: ')

        hobby=input('enter your hobby: ')

        password=input('enter your password: ')

        pattern=("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])");

        for i in password:
        
            if len(password)>=6 and len(password)<=12:

                if not re.search('[A-Z]', password):

                    print('please include a upper case letter')

                    break

                if not re.search('[a-z]', password):

                    print('please include a lower case letter')

                    break

                if not re.search('[0-9]', password):

                    print('please include a digit')

                    break

                if not re.search('[!@#\$%\^&\*]', password):
                
                    print('please include a special charector')

                    break
                    

                else:

                        print('strong pass')

                        break

            else:
                print('wrong length')

                password=input('enter your  password again : ')

                pattern=("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])");

                for i in password:
                
                    if len(password)>=6 and len(password)<=12:

                        if not re.search('[A-Z]', password):

                            print('please include a upper case letter')

                            break

                        if not re.search('[a-z]', password):

                            print('please include a lower case letter')

                            break

                        if not re.search('[0-9]', password):

                            print('please include a digit')

                            break

                        if not re.search('[!@#\$%\^&\*]', password):
                        
                            print('please include a special charector')

                            break
                            

                        else:

                                print('strong pass')

                                break

                    else:
                        print('wrong length')
                        
                        break

        confirmpass=input('confirm your password:')

        dic1={'Username':username,'PhoneNo':phoneNo,'Age':age,'Description':description,'Hobby':hobby,'Password':password}

        a=open("Login_system.json",'r')

        list1=json.load(a)

        list1.append(dic1)

        if password==confirmpass:

            print('Registration successfuly')

            my_file=open("Login_system.json",'w')

            json.dump(list1,my_file,indent=6)

        else:

            print('Registration failed! please confirm your password correct')

    elif choose=='login':

        username=input('enter your name: ')

        password=input('enter your password: ')

        pattern=("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])");

        for i in password:

            if len(password)>=6 and len(password)<=12:
    
                    if not re.search('[A-Z]', password):

                        print('please include a upper case letter')

                        break

                    if not re.search('[a-z]', password):

                        print('please include a lower case letter')

                        break

                    if not re.search('[0-9]', password):

                        print('please include a digit')

                        break

                    if not re.search('[!@#\$%\^&\*]', password):
                    
                        print('please include a special charector')

                        break
                        

                    else:

                            print('strong pass')

                            break

            else:
                print('wrong length')
                
                password=input('enter your  password again : ')

                pattern=("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])");

                for i in password:
                
                    if len(password)>=6 and len(password)<=12:

                        if not re.search('[A-Z]', password):

                            print('please include a upper case letter')

                            break

                        if not re.search('[a-z]', password):

                            print('please include a lower case letter')

                            break

                        if not re.search('[0-9]', password):

                            print('please include a digit')

                            break

                        if not re.search('[!@#\$%\^&\*]', password):
                        
                            print('please include a special charector')

                            break
                            

                        else:

                                print('strong pass')

                                break

                    else:
                        print('wrong length')
                        
                        break

        my_file=open("Login_system.json",'r')

        a=json.load(my_file)

        b={}

        def login_or_not(username,password,a,b):

            for i in a:
                   print(i)
                   if i['Username']==username and i['Password']==password:

                            b.update(i)

                            for k,v in b.items():
    

                                print(k,'is -',v)     

                            print('login successfuly....')
                        
                   else:

                        print('login failed! please enter your correct info....')

                        
        Data=login_or_not(username, password,a,b)
        
        # if Data:

        #     print(Data)
            
        #     print('login successfuly....')

        # else:
        #         print('login failed! please enter your correct info....')
    else:
        
        print('incorrect') 

else:

    print('incorrect')





    


# import re


# strong=("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])");

# password=input('enter your passwoed: ')

# for i in password:

#         if len(password)>=6 and len(password)<=12:
            
#                 if re.search('[A-Z]', password):

#                     if re.search('[a-z]', password):

#                         if re.search('[0-9]', password):

#                             if re.search('[!@#\$%\^&\*]', password):
                    
#                                     print('strong')
#                                     break
#                             else:
#                                 print('wrong pass. include a special charector')
#                                 break
#                         else:
#                             print('include a digit')
#                             break
#                     else:
#                         print('include a lower case letter')
#                         break
#                 else:
#                     print('include a upper case letter')
#                     break
#         else:
#             print('wrong length')

#             break
#             confirm=input('enter')

#             if password==confirm:

#                         print('asfg')
        # else:

                # print('strong pass')

                # break

    # else:
    #     print('wrong length')

    #     string=input('enter your passwoed: ')

    #     for i in string:

    #         if len(string)>=6 and len(string)<=12:

    #             if not re.search('[A-Z]', string):

    #                 print('please include a upper case letter')

    #                 break

    #             if not re.search('[a-z]', string):

    #                 print('please enter a lower case letter')

    #                 break

    #             if not re.search('[0-9]', string):

    #                 print('please enter a digit')

    #                 break

    #             if not re.search('[!@#\$%\^&\*]', string):
                
    #                 print('please enter a special charector')

    #                 break
                    

    #             else:

    #                     print('strong pass')

    #                     break

    #         else:
    #             print('wrong length')

    #             break