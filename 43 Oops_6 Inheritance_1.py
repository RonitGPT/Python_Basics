#==========================================================================================================
                                        # INHERITANCE
#==========================================================================================================
'''
INHERITANCE creates a new class with the help of properties of base class 
It has a IS-A relationship 
Provides Code reusability

Syntax :- 
        class subclass(superclass):
'''

class Father ():
    def Farm(self):
        print ("Farm ......")

class Child (Father):
    def House(self):
        print ("House ......")

c = Child()

# Using Inheritance Child class can access functions of its own class as well as superclass
c.Farm()
c.House()