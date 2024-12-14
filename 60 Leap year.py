#==========================================================================================================
                                # PROGRAM TO FIND IF YHE YEAR IS LEAP YEAR 
#==========================================================================================================

x = int(input("Enter the Year :- "))

if ((x%4 == 0) and (x%100 != 0)  or x%400 == 0) :
    print(f"The year {x} is a Leap Year")
else:
    print(f"The year {x} is a not a Leap Year")

