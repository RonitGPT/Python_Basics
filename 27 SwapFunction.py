    # PROGRAM TO SWAP TWO NUMBERS WITHOUT USING VARIABLES

def swap(a,b):
    print("Before Swapping a = ", a)
    print("After Swapping a = ", b)
    a = a+b
    b = a-b
    a = b-a
    print("************************************")
    print("After Swapping a = ", a)
    print("After Swapping a = ", b)

a = int(input("Enter the number a :- "))
b = int(input("Enter the number b :- "))

swap(a,b)