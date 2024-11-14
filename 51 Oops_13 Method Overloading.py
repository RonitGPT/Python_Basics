#==========================================================================================================
                                        # METHOD OVERLOADING 
#==========================================================================================================
'''
METHOD OVERLOADING --> Same method , same class but different Parameters 
But python does not supports the method overloading method 
as it gives mising required positional arguiment error 
'''
class Add():
    def get(self,a,b):
        self.a = a
        self.b = b
        r1 = self.a + self.b
        print ("Sum of 2 digits is :- ", r1)

    def get(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        r2 = self.a + self.b + self.c
        print ("Sum of 3 digits is :- ", r2)

a = Add()
a.get(2,3)
a.get(3,4,5)