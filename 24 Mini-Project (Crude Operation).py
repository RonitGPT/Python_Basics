#=====================================================================================================
                                        # CRUDE OPERATIONS
#=====================================================================================================
List = []
#------------------------------------------------------------------------------------------------------

# Functions 

def add_item():
    name = input("Enter name of the Item :- ")
    price = float(input("Price of the Item :- "))
    new_item = (name, price)
    List.append(new_item)
    print("The item '{}' with price '{}' was succesfully added ".format(name, price))

def show_item():
    if not List:
        print("Your List is empty")
    else :
        print("Your List contains :- ")
    for i,X in enumerate (List , 0):
    
        print("{}. {}-{} ".format(i. X['name'],X['price']))
    '''
    print ("\n" , List(name, price))
    '''

def delete_item():
    pass

def update_item():
    pass


while True:
    print("***** MENU *****")
    print("1. ADD ITEMS")
    print("2. SHOW ITEMS")
    print("3. REMOVE ITEMS")
    print("4. UPDATE ITEMS")
    print("5. EXIT ")

    choise = input("Enter the Operation Number :- ")

    if (choise == "1"):
        add_item()
    elif (choise == "2"):
        show_item()
    elif (choise == "3"):
        delete_item()
    elif (choise == "4"):
        update_item()
    elif (choise == "5"):
        print("Exiting")
        break
    else :
        print("Invalid Choice")
    
    ans = input("If you want to continuee.. enter 'y' :- ")
    if (ans.lower()!= "y"):
        break