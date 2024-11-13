#==========================================================================================================
                                        # POLYMORPHISM
#==========================================================================================================
'''
POLY ----> Many 
MORPHISM ----> Forms 
POLYMORPHISM ----> Ability to take Many Forms 
        There are 2 Types :- 
            1. METHOD OVERLOADING ( Not supportes by python ) :- 
                                        same method , different parameters and same classes
            2. METHOD OVERRIDING ( Supported by python ) :-
                                        same method , same parameters and different classes


    # CONSTRUCTOR OVERRIDING --> same constructor name , same parameter but different classes

class A():
    def __init__(self):
        self.a = int(input("Enter the number a :- "))

class B(A):
    def __init__(self):
        self.b = int(input("Enter the number b :- "))
        super().__init__()   # Accessing Parent Class 

    def Add(self):
        result = self.a + self.b
        print(result)

b = B()
b.Add()
'''
#--------------------------------------------------------------------------------------------------------------------------------

    # METHOD OVERRIDING --> Same method, same parameter , different class 

class Main():
    def get_main(self):
        self.a = int(input("Enter the number a :- "))

class Mult(Main):
    def get_main(self):
        self.b = int(input("Enter the number b :- "))
        super().get_main()

    def Product(self):
        result = self.a * self.b
        print("The product is :- ", result)

m = Mult()
m.get_main()

m.Product()