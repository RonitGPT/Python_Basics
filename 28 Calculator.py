        # PROGRAM TO MAKE A CALCULATOR 

def add(a,b):
    return a+b 

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("************* WELCOME TO MY CALCULATOR *************")

while True:
    print(" 1. ADDITION ")
    print(" 2. SUBTRACTION ")
    print(" 3. MULTIPLICATION ")
    print(" 4. DIVISION ")
    print(" 5. QUIT ")

    choice = int(input("Enter your choice for operation :- "))
    
    if choice == 5:
        print("Thank you so much :) !!!.....")
        break
    else :
        x = int(input("Enter your number x :- "))
        y = int(input("Enter your number y :- "))

    if choice == 1:
        r1 = add(x,y)
        print("The Addition is :- ", r1)
    elif choice == 2:
        r2 = sub(x,y)
        print("The Subtraction is :- ", r2)
    elif choice == 3:
        r3 = mul(x,y)
        print("The Product is :- ", r3)
    elif choice == 4:
        r4 = div(x,y)
        print("The Division is :- ",r4)

    ans = input("If you want to continue press 'y' :- ")
    if (ans.lower()!= 'y'):
        break

    
    


    