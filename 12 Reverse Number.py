    # PROGRAM TO FIND THE REVERSE NUMBER 

x = int(input(" Enter the number :-  "))
Sum = 0
while (x > 0):
    y = x % 10
    Sum = Sum * 10 + y
    x = x // 10
print (" Your Reversed number is :- " , Sum)
