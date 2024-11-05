#===================================================================================================================================
                                                #  RECCURSION FUNCTIONS
#===================================================================================================================================
'''
RECCURSION FUNCTION means to use function indide the funcion 

'''

    # PROGRAM TO FIND FACTORIAL OF NUMBER USING RECCURSION FUNCTIONS

def Factorial(x):
    if x == 1:
        return 1 
    else :
        return (x * Factorial(x-1))

x = int(input("Enter the number x :- "))
print ("The Factorial is :- ", Factorial(x))


    