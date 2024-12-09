#==========================================================================================================
                                        # CUSTOM EXCEPTION
#==========================================================================================================
'''
CUSTOM EXCEPTION ---> They are user defined exceptions
    Syntax :- 
            class UserDefinedException(Exception):
'''

class Invalid_age(Exception):
    pass

try:
    x = int(input("Enter your Age :- "))
    if x >= 18 :
        print("You are Eligible for voting ")
    else :
        raise Invalid_age
    
except Invalid_age:
    print("You are 'NOT' Eligible for Voting ")

#================================================================================================================================

password = "Yash491"

class password(Exception):
    pass

try:
    x = input("Enter your Password :- ")
    if x == password:
        print("You have successfully entered your password")
    else:
        raise password
    
except password:
    print("Invalid Password ")