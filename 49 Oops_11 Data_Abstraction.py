#==========================================================================================================
                                        # DATA ABSTRACTION
#==========================================================================================================
'''
DATA ABSTRACTION --------> Hiding Internal Details and showing main sunctionalities 
1. Concreate Method ------> Which is the actual method Execution 
2. Abstract Method ------> Which is Method Declaration Only 
So we can't creat object of abstract class 
'''
class Fruit ():
    def Color(self):
        pass
    def Taste(self):
        pass

class Apple ():
    def Color(self):
        print("Apple is Red...")
    def Taste(self):
        print("Apple is Tangy...")


class Mango ():
    def Color(self):
        print("Mango is Yellow...")
    def Taste(self):
        print("Mango is Sweet...")

a = Apple()
a.Color()
a.Taste()

m = Mango()
m.Color()
m.Taste()