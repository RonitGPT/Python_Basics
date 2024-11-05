#===================================================================================================================================
                                                #  FUNCTIONS
#===================================================================================================================================

def greet_msg():
    print("HELLO ... Good Morning !.....")
    print("Welcome to Python !.....")
    print("Welcome to Django !.....")

greet_msg()
greet_msg()
greet_msg()

# program to find cube using functions 

def cube(x):                     # Function Delclaration
    a = x*x*x                    # Function Body
    print("The cube is ", a)

cube(34)                         # Call Function

# program to find square using functions 

def square(y):
    return y*y

print("The square is ", square(12))
print("The square is ", square(9))
print("The square is ", square(132))

