#===================================================================================================================
                                        # TUPLE DATATYPE
#===================================================================================================================

'''
TUPLE DATATYPE ----> IT IS IMMUTABLE DATATYPE (NON-CHANGABLE DATATYPE)
TUPLE cannnot perform INSERT DELETE OPERATIONS
It is represented by ()
'''
#------------------------------------------------------------------------------------------------------------------

tuple1 = ('manasi', 'pradnya', 'niharika', 'simran', 'chaitali', 'usha')

#------------------------------------------------------------------------------------------------------------------

# To print tuple
print(tuple1)

# To check the length of tuple
print(len(tuple1))

# To nd the maximum string in tuple
print(max(tuple1))

# Toprint minimum string in tuple
print(min(tuple1))

# Slicing in tuple
print(tuple1[1:4])

# To change the datatype
result = list(tuple1)
print(result)
