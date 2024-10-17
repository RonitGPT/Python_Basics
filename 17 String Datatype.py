'''
More Data types in python ----> String , List , Tuple , disctionary 
1. String data types are ----> Sequece of character placed in ''," ", ''' '''
inbuild function in string
'''

str = "itvedant Thane" 
str2 = "hello"
list1 = ['1','2','3','4','5']
print (str.capitalize())         # Display first alpha in capital
print(str.upper())
print(str.lower())

print(str.title())             # Display every word's first alpha in capital

print(str.isupper())
print(str.islower())

print(len(str))

print(str.swapcase())

print(str.isalpha())
print(str2.islower())

result= str.join(list1)
print(result)

print(min(str))
print(max(str))

print(str.replace('Thane','Mumbai'))



