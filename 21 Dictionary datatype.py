#=================================================================================================
                                    # DICTIONARY DATATYPE
#=================================================================================================
'''
DICTIONARY DATATYPE
IT CONTAINS DATA IN FORM OF KEYS AND VALUES
IT IS USED WHEN WE HAVE LARGE DATA
IT IS REPRESENTED IN {}
'''
#--------------------------------------------------------------------------------------------------
dict1 = {'Name':'Ronit' , 'Age':'21' , 'Address':'Thane'}
#--------------------------------------------------------------------------------------------------

# To print the Dictionary
print(dict1)

# To print the length of dictionary
print("Te Length is" , len(dict1))

# To print the type
print("The type is" , type(dict1))

# To convert the datatype
print("The Converted Datatype is " ,str(dict1))

# To print keys of Dictionary 
print("The keys are " , dict1.keys())

# To print values of Dictionary
print("The values are ", dict1.values())

# To copy Dictionary
dict2 = dict1.copy()
print("The copied dict is " , dict2)

# To add data
dict1 = ['Contact no'] = 9372692475
print(dict1)

# To remove data
dict1.pop('contact no')
print(dict1)

# To clear all data
dict2.clear()
print(dict2)


