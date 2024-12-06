#==========================================================================================================
                                        # TRY - EXCEPT - FINALLY
#==========================================================================================================

        # THE FINALLY BLOCK WILL ALWAYS SHOW THE CONTENT INSIDE IT 

try:
    A = int(input("Enter the number A "))
    B = int(input("Enter the number B "))
    C = A / B 
    print(C)

except ZeroDivisionError:
    print("ZeroDivisionError")
    print("Done")

except ValueError:
    print("ValueError --> Wrong Input Value")
    print("Done")

finally:
    print("Hii I'm Finally block ")
