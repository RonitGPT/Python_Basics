#===================================================================================================================
                                    # LIST DATATYPE
#===================================================================================================================

'''
LIST DATATYPE -----> IT IS MUTABLE DATATYPE (CHANGABLE DATATYPE)
LIST are collection of different types of data
They are represented by []
'''
#------------------------------------------------------------------------------------------------------------------

List1 = [ "Ronit", "Manasi", "Vishal", "Yash", "Niharika", "Pradnya", "Chaitali","Sushant", "Aakash" ]

#------------------------------------------------------------------------------------------------------------------

# To print element of list
print(List1)

# To print lenght of list
print(len(List1))

# To print Maximum string in list
print (max(List1))

# To print Minimun string in list
print(min(List1))

# To print first element in list
print(List1[0])

# Slicing in list
print(List1[1:4])

# To add item in list
List1.append("Nitin")
print(List1)

# To remove item from list
List1.pop(7)
print(List1)

# To reverse item in List
List1.reverse()
print(List1)
