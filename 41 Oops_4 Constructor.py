#=======================================================================================================
                                        # CONSTRUCTOR 
#=======================================================================================================

'''
In Python, a constructor is a special method called __init__() that's automatically invoked 
when a new instance of a class is created. It's primarily used to initialize the object's attributes with
specific values.

'''

class book():

    def __init__(self,b_id , b_name, b_price ,b_Author):
        self.b_id = b_id
        self.b_name = b_name
        self.b_price = b_price
        self.b_Author = b_Author

    def result(self):
        print ("The ID if the Book is ", self.b_id)
        print ("The Name if the Book is ", self.b_name)
        print ("The Price if the Book is ", self.b_price)
        print ("The Author if the Book is ", self.b_Author)

b_id = int(input("Enter the Book ID: "))
b_name = input("Enter the Book Name: ")
b_price = int(input("Enter the Price of the Book: "))
b_Author = input("Enter the Name of the Author: ")

s = book(b_id , b_name , b_price , b_Author)

# To display the result 
s.result()