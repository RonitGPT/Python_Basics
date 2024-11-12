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
                            # 4 MULTIPLE INHERITANCE
#----------------------------------------------------------------------------------------------------------

# In MULTIPLE INHERITANCE is THERE ONLY ONE SUBCLASS AND MANY SUPERCLASS RELATED TO SUBCLASS

class Grandfather:
    def Farm(self):
        print("Farm.....")

class Father:
    def House(self):
        print("House.....")

class Child (Father,Grandfather):
    def Car(self):
        print("Car.....")

# ACCESSING THE DATA 

c = Child()
c.Farm()
c.House()
c.Car()