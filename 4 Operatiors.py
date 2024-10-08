# ARITHMATIC OPERATORS ------------> ( =,-,*,/,%,//)

a=int(input("Enter the First no = "))
b=int(input("Enter the Second no = "))

Sum = a+b
Diff = a-b
Product = a*b
Division = a/b
Mod = a%b
Floor_Div = 23//5

print(Sum)
print(Diff)
print(Product)
print(Division)
print(Mod)
print(Floor_Div)

#-----------------------------------------------------------------

# COMPARISON OPERATORS -----------> ( <,>,<=,>=,!= )

a=int(input("Enter First No = "))
b=int(input("Enter Second No = "))

print(a>b)
print(a<b)
print(a>=b)
print(a>=b)
print(a!=b)

#------------------------------------------------------------------

# LOGICAL OPERATORS -------------> ( and,or,not )

a=int(input("Enter First No = "))
b=int(input("Enter Second No = "))
c=int(input("Enter Third No = "))
print("********** AND OPERATORS *************")
print( (a>b) and (b>c) )
print( (a<b) and (b<c) )
print("********** OR OPERATORS *************")
print( (a>b) or (b>c) )
print( (a<b) or (b<c) )
print("********** NOT OPERATORS *************")
print( not (a>b) or (b>c) )

#-------------------------------------------------------------------

# ASSIGNMENT OPERATORS

a=int(input("Enter First No = "))

a+=34    # a=a+34
a-=34    # a=a-34
a*=34    # a=a*34
a/=34    # a=a/34
a%=34    # a=a%34

#-------------------------------------------------------------------

# DIFFERENCE BETWEEN '=' AND '==' IS ----> '=' IS USED TO ASSIGN VALUES -- '==' IS USED TO COMPARE VALUES

#--------------------------------------------------------------------

# USE OF TYPE OPERATORS ---> type() ----------> Used to check datatype

print(type(34))
print(type(63.4))
print(type("Ram"))
print(type("Vishal491"))
print(type(9372697424673873))
print(type(True))
