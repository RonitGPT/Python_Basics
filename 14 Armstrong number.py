#==========================================================================================================
                    # PROGRAM TO FIND IF THE NUMBER IS PELLINDROME OR NOT (ONLY FOR 3 DIGITS)
#==========================================================================================================

x = int (input("Enter the numbe 'x :- " ))
n = x
sum = 0
while (x>0):
    y = x % 10
    a = y*y*y
    sum = sum + a
    x = x // 10
if (sum == n):
    print ("Number is ARMSTRONG")
else:
    print ("Number is NOT ARMSTRONG")

    
