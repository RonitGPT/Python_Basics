#===================================================================================================================================
                                                #  MAP  FUNCTIONS
#===================================================================================================================================

'''
MAP FUNCTIONS --> it executes the given function with iterables 
SYNTAX :- 
        map(function,iterable)---> map object 

'''
def square (x):
    return x*x

t = [1,3,5,7,9,2,4,6,8]

result = map(square , t)
x = set(result)
print(x)

# using lamda function
a = map(lambda y: y*y ,t)
b = list(a)
print(b)

