 # FOR LOOP
#=============================================================================

 # Program to display numbers from 1 to 10

for i in range(1,11):
    print(i)

#-----------------------------------------------------------------------------

 # Program to display numbers from 10 to 1 in reverse order

for i in range(10,0,-1):
    print(i)

#-----------------------------------------------------------------------------

 # Program to display table of 2

for i in range(2,21,+2):
    print(i)

#-----------------------------------------------------------------------------

 # Program to display numbers upto n numbers

n=int(input("Enter the number n = "))
for i in range(1,n+1):
    print(i)

#-----------------------------------------------------------------------------

 # Program to display table of n number

n=int(input("Enter you number = "))
for x in range(1,11):
    print(n,"*",x,"=",x*n)
