#==========================================================================================================
                                        # TYPES OF INHERITANCE
#==========================================================================================================
'''
THERE ARE 5 TYPES OF INHERITANCE:-
    1. single inheritance
    2. multilevel inheritance
    3. heirarchical inheritance
    4. multiple inheritance
    5. hybrid inheritance
'''

#----------------------------------------------------------------------------------------------------------
                            # 3. HEIRARCHICAL INHERITANCE
#----------------------------------------------------------------------------------------------------------

# In Heirarchical inheritance there are many Subclasses and only single Superclass

# Superclass
class Grandfather():
    def Farm(self):
        print("Farm.....")

# Subclass
class Father(Grandfather):
    def House(self):
        print("House.....")

# Subclass
class Child(Grandfather):
    def Car(self):
        print("Car.....")

# Accessing the data 
print("***** Child Property *****")
c= Child()
c.Car()
c.Farm()

print("***** Father Property *****")
f = Father()
f.Farm()
f.House() 