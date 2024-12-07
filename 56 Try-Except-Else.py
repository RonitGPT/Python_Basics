#==========================================================================================================
                                        # TRY - EXCEPT - ELSE
#==========================================================================================================

    # Else block will be executed if there is no exceptions in try block 

try:
    A = int(input("Enter the number A "))
    B = int(input("Enter the number B "))
    C = A / B 

except ZeroDivisionError:
    print("ZeroDivisionError")
    print("Done")

except ValueError:
    print("ValueError --> Wrong Input Value")
    print("Done")

else:
    print("Division is :- ", C)