#===================================================================================================================================
                                    #  ANONYMOUS FUNCTIONS / LAMBDA FUNCTIONS
#===================================================================================================================================

'''
Anonymous Functions -----> Function Having no name 
Also known as "LAMBDA functions"

SYNTAX :- 
        lambda (parameter):
                code
'''
    # PROGRAM TO FIND SQAURE OF A NUMBER 

#using normal functions
def square(x):
    return x * x
print("square is  " , square(5))

#using lambda functions
a = int(input("Enter your number a :- "))
result = lambda y : y*y 
print ("square is " , result(a))

# Addition of three numbers
a = int(input("Enter your number a :- "))
b = int(input("Enter your number b :- "))
c = int(input("Enter your number c :- "))
result1 = lambda a,b,c : a+b+c
print ("Addition od three numbers is " , result1(a,b,c))