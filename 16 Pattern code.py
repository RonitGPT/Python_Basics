        # PATTERN USING PYTHON 
'''
NESTED LOOP :- LOOP INSIDE THE LOOP 
SYNTAX :- 
OUTER LOOP:
    INNER LOOP
'''
#================================================================================================================
                            # PATTERNS
#================================================================================================================

    # PATTERN 1

x = int(input("Enter the number x :- "))
for i in range (1,x+1):
    for j in range (1,i+1):
        print("*" , end = "")
    print ()

'''
Enter the number x :- 5
*
**
***
****
*****
'''
#-----------------------------------------------------------------------------------------------------------------

    # PATTERN 2

x = int(input("Enter the number x :- "))
for i in range (1,x+1):
    for j in range (1,x+1):
        print("*" , end = " ")
    print ()

'''
Enter the number x :- 5
* * * * * 
* * * * *
* * * * *
* * * * *
* * * * *
'''
#------------------------------------------------------------------------------------------------------------------

    # PATTERN 3

x = int(input("Enter the number x :- "))
for i in range (1,x+1):
    for j in range (1,i+1):
        print(i , end = " ")
    print()

'''
Enter the number x :- 5
1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
#-------------------------------------------------------------------------------------------------------------------

    # PATTERN 4

x = int(input("Enter the number x :- "))
for i in range (1,x+1):
    for j in range (1,i-1):
        print (i , end = ' ')
    print()

'''
Enter the number x :- 5


3
4 4
5 5 5
'''
#-----------------------------------------------------------------------------------------------------------------

    # PATTERN 5

x = int(input("Enter the number x :- "))
for i in range (x ,0,-1):
    for j in range (i ,0 ,-1):
        print("*" , end = ' ')
    print()
'''
Enter the number x :- 5
* * * * * 
* * * *
* * *
* *
*
'''