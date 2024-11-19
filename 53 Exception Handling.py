#===================================================================================================================================
                                                #  Exception Handling 
#===================================================================================================================================

'''
Exception Handling ---> They are Runtime Error 
print("Welcome Python) ---> This is user ceated error(Compile Time) in which " is not present
    Types :- 
        1. ZeroDivisionError : If we divide number by zero 
        2. ValueError 
    Solution :- 
        We can use try Except block for handling this issue 

TRY :- Indicate Exceptional code 
Except :- Handle the Exception 
Finally :- Always execute whether exception handled or not ( file close , database close )
Else :- When there is no any exception in your Try block then else block work 
Raise :- Pass the exception to except block
Exception :- It is already defined class in python ( Base class)

'''

        # TRY EXCEPT BLOCK HANDLING 

try:
    A = int(input("Enter the number A :- "))
    B = int(input("Enter the number B :- "))
    C = A / B
    print("The Dision is ", C)

except Exception:
    print("ZeroDivisionError")

print('Done')