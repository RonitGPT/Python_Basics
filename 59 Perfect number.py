#==========================================================================================================
                                    # PROGRAM TO FIND PERFECT NUMBERS 
#==========================================================================================================

x = int(input("Enter the number :- "))
n = x
sum = 0 
for i in range (1,x):
    if x%i == 0 :
        sum = sum + i 

if sum == n :
    print (f"The number {x} is a Perfect number ")
else:
    print (f"The number {x} is a NOT a Perfect number ")
