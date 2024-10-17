'''
LIST  data type ---->  It is Mutable Data Type i.e ( CHANGEABLE Datatype)
Lists are represented by []
List are collection of different types of data
'''
'''
list1 = [ 1, "Vishal", 25 , 96.75 , "M" , "M"]
list2 = [ "JAVA","SQL" , "PYTHON"]

print (len(list1))
s= list2.reverse(list1)
print(s) 

k = list1.count("M")
print(k)

list2.append("DJANGO")
print(list2)

print(min(list2))
print(max(list2))
'''

# ------------------------------------------------------------------------------------------------------
list1 = ['vishal', 'yash','ronit', 'manasi','akash','nitin']

print("element in list - " , list1)
print("length of list -" , len(list1))
print("Maximum str in list - ", max(list1))
print("Minimum str in list - ", min(list1))
print("First element in list - ", list1[0])
print("Slicing in list - ", list1[1:4])
list1.append("sushant")
print("APPENDED LIST IS - ", list1)
list1.pop(1)
print("Removed element is - ", list1)
list1.reverse()
print("Reversed element is - ", list1)






