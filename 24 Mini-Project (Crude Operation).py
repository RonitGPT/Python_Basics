#=====================================================================================================
                                        # CRUDE OPERATIONS
#=====================================================================================================

List = []

def add_item():
    print("Add Item")

def show_item():
    print("Show Item")

def delete_item():
    print("Delete Item")

def update_item():
    print("Update item")

while True :
    print("*** MENU ***")
    print("1. Insert Item ")
    print("2. Show Item ")
    print("3. Delete Item ")
    print("4. Update Item ")
    print("5. Exit ")

    choose = input("Enter Number to perform Operation :- ")

    if (choose == '1'):
        add_item()
    elif (choose == '2'):
        show_item()
    elif (choose == '3'):
        delete_item()
    elif (choose == '4'):
        update_item()
    elif (choose == '5'):
        break
    else :
        print ("Invalid Option")

    ans = input("Do you want to Continue.. Press 'yes' :- ")
    if (ans.lower()!= "yes" ):
        break
    
    
    
