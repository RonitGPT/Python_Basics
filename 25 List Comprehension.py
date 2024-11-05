#===================================================================================================================================
                                                #LIST COMPREHENSION
#===================================================================================================================================
'''
List Comprehension - It is used to make the lenght of code shorter 
it creates list with the help of another list 
'''
#------------------------------------------------------------------------------------------------------------------------------------
Language = ['Pythons' , 'SQL' , 'Django' , 'HTML' , 'JavaScript' , 'CSS', 'Flask' , 'React' ]
#------------------------------------------------------------------------------------------------------------------------------------

# to add content of language containing letter a in newlist 
newlist = []
for  x in Language :
    if "a" in x :
        newlist.append(x)
print (newlist)

# to print content of language 
y = []
for y in Language:
    print (y)

#-----------------------------------------------------------------------------------------------------------------------------------

# USING LIST COMPREHENSION 
# SYNTAX  :- [ expression for items in iterable if condition = True ] 

Language1 = ['Pythons' , 'SQL' , 'Django' , 'HTML' , 'JavaScript' , 'CSS', 'Flask' , 'React' ]
newlist = [ x for x in Language1 if "a" in x]
print(newlist)

num = [1,2,3,4,5,6,7,8,9]
a = [ y*2 for y in num]
print (a)

w = [x for x in Language1]
print (w)