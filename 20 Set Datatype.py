#=================================================================================================
                                    # SET DATATYPE
#=================================================================================================
'''
SET DATATYPE :- IT IS MUTABLE DATATYPE
IT IS USED TO STORE DATA
IT ALWAYS CONTAINS DISTINCT DATA
IT IS REPRESENTED BY {}
IT IS UNORDERED COLLECTION OF DATA
'''
#--------------------------------------------------------------------------------------------------
set1 = { 3,5,8,7,9,6,1,4,2 }
set2 = { 3,6,9,12,15,18,21 }
#--------------------------------------------------------------------------------------------------

# To print set datatype
print (set1)
print (set2)

# To check the length of sets
print("Length is ", len(set1))
print("Length is ", len(set2))

# To add item into set datatype
set1.add(12)
set2.add(24)
print ("After adding data",set1)
print ("After adding data",set2)

# To remove data fron Set Datatype        (Removes first item)
set1.pop()
set2.pop()
print("After pop operation", set1)
print("After pop operation", set2)

# To remove data fron Set Datatype
set1.remove(7)
set2.remove(12)
print("After remove operation", set1)
print("After remove operation", set2)

# To perform union operation (join data of two sets)
result1 = set1.union(set2)
print("After union operation" , result1)

# To perform intersection (displays common elements only)
result2 = set1.intersection(set2)
print("After intersection operation", result2)


