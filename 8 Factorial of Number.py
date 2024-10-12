    # PROGRAM TO FIND THE FACTORIALOF NUMBER 

x = int(input("ENTER YOUR NO :- "))
Fact = 1 
for i in range (1 , x + 1): 
    Fact = Fact * i 
    i = i + 1 
print ("Factorial of ",x," is = ",Fact)   