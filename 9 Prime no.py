    # PROGRAM TO FIND IF THE GIVEN NUMBER IS PRIME NUMBER OR NOT 

x = int(input(" ENTER THE NUMBER = "))
count = 0 
for i in range(1, x+1):
    if (x % i == 0):
        count = count + 1
if (count == 2):
        print ("Number is Prime number")
else :
        print ("Number is not prime number")

                
