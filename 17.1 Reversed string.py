#==========================================================================================================================
                                    # Python program to reverse the string 
#==========================================================================================================================

'''
if 
str = " we are learning python strings "
then output will be 
output = " strings python learning are we "

'''
a = input("Enter the sentence :- ")
a = a.split()
b = (list(reversed(a)))
c = " ".join(b)
print(c)