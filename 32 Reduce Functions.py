#===================================================================================================================================
                                                #  REDUCE FUNCTIONS
#===================================================================================================================================

'''
MAP FUNCTIONS ---> it is an inbuild function in python 
applies in iterable items 
Always returns result in single values 
Syntax :- 
        fron functools import reduce 
            reduce (function,iterable)

'''
from functools import reduce 

def add(a,b):
    return a + b

t = [1,3,5,7,9,8,6,4,2]

result = reduce (add,t)
print(result)

# using lambda function 
x = reduce (lambda a,b : a+b ,t)
print ("The addition is :- " , x)

# program to find the highest number from list 
List = [12,45,53,64,48,85,4,65,75,65,8,95,54,67,23,66]

greater = reduce (lambda a,b : a if a>b else b , List)
print("The greater number is :- ", greater)