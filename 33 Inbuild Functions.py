#===================================================================================================================================
                                                #  INBUILD  FUNCTIONS
#===================================================================================================================================
'''
INBUILD FUNCTIONS (MODULES) ---> math , sys , os , datetime , random , calender
'''
# Math functions

import math as m 

# factorial , ceil , floor , square(sqrt) , pi , power(pow)
print ("Factorial is :- " , m.factorial(8))
print (" ceil is :- " , m.ceil(7.6))
print (" floor is :- " , m.floor(8.4))
print (" square is :- " , m.sqrt(5))
print (" power is :- " , m.pow(5,6))
print (" pi value is :- " , m.pi)

#---------------------------------------------------------------------------------------------------------------------------

#DATETIME FUNCTIONS

import datetime as d
import time as t

print (d.datetime.now())
print(d.date.today())
print(t.localtime())

tk = t.localtime()

print("Calender yer is :- ", tk.tm_year)
print("Calender Month is :- ", tk.tm_mon)
print("Calender Day is :- ", tk.tm_mday)

#----------------------------------------------------------------------------------------------------------------------------

# CALENDER FUNCTION 

import calendar 

c = calendar.TextCalendar(calendar.MONDAY)
c.prmonth(2024,10)

#-----------------------------------------------------------------------------------------------------------------------------

# Random Function 

import random

mylist =["java","python","Ruby","c++", "sql","django"]

for i in range(6):
    print(random.choice(mylist))

#==========================================================================================================================

# AREA OF CIRCLE USING MATH FUNCTION 

import math as m 
def area(x):
    return m.pi*x*x
x = float(input("Enter the radius :- "))
print("The area is = ", area(x))

# Return duplicates element in list 

number2 = [1,2,3,4,3,2,1,6,7,8,5,9,8,9]

x = filter(lambda x : number2.count(x) == 1, number2)
print("uniques is :- ", list(x))

y =number2
z = set(y).union(set(number2))
print("Intersection is :- " , list(z))

# PROGRAM TO PRINT ONLY POSITIVE NUMBERS 
number = [1,2,3,4,7,-3,-3,-5,-7 ]

a = filter (lambda x : x>0 , number)
print("Positive numbers are :- ", list(a))