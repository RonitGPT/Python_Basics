#==========================================================================================================
                        # PROGRAM TO FIND IF THE NUMBER IS PELLINDROME
#==========================================================================================================

x = int(input("Enter your number x = "))
n=x
sum=0
while (x>0):
    y = x % 10
    sum = sum*10 + y
    x = x // 10
if (sum == n):
    print("Number is PELLINDROME")
else:
    print("Number is NOT PELLINDROME")
