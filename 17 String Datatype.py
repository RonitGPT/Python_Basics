#==========================================================================================================================
        # MORE DATA TYPES ON PYTHON :- STRING , LIST , TUPLE , DICTIONARY , SET.
#==========================================================================================================================

    # STRING DATATYPE

'''
STRING DATATYPE :- Sequence of characters placed in ' ', " " , """ """ .
Inbuild function string
'''

str1 = "itvedant thane"
str2 = " hello "

#------------------------------------------------------------------------------------------------------------------------

print(str1.capitalize())      # Display first letter in Capital
print(str1.upper())
print(str1.lower())

print(str1.title())           # Display every word's first letter in capital

print(str1.isupper())
print(str1.islower())

print(len(str1))

print(str1.swapcase())

print(str1.isalpha())
print(str1.islower())

result = str1.join(str2)
print(result)

print(min(str1))
print(max(str1))

print(str1.replace("thane", "Mumbai"))
