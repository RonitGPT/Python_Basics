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
                            # 2.MULTILEVEL INHERITANCE
#----------------------------------------------------------------------------------------------------------

# In this one class is related to another class which is related to anothe class 

class Grandfather():
    def Farm(self):
        print("Farm.....")

class Father(Grandfather):
    def House(self):
        print("House.....")

class Child(Father):
    def Car(self):
        print("Car.....")

c = Child()
c.Car()
c.House()
c.Farm()