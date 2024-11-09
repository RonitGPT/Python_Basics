#=======================================================================================================
                                        # DESTRUCTOR
#=======================================================================================================
'''
In Python, a destructor is a special method that is automatically invoked when an object is about to be 
destroyed. The destructor method in Python is named __del__(), and it's part of the class. When the 
program execution goes out of the scope where the object was created, Python's garbage collector will
automatically clean up the object and call the __del__() method if it's defined.

'''

class demo():
    def __init__(self):
        print("This is default constructor calling")
    def __del__(self):
        print("This is default destructor calling")

c = demo()
del c