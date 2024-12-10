#==========================================================================================================
                                        # ENCAPSULATION
#==========================================================================================================
''' 
ENCAPSULATION --> Wrapping data into single unit 

    Types :- 
            1. Public Data Member
            2. Protected Data Member
            3. Private Data Member
'''
                # Protected data member example 

class Student():
    _id = 100
    _name = "David Smith"

class Trainer (Student):
    def __init__(self):
        print("The ID of the Student is :- ", self._id)
        print("The name of the Student is :- ", self._name)

s = Trainer()

#============================================================================================================================

                # Private data member example

class Book():
    def __init__(self,b_id,b_name,b_author):
        self.__b_id = b_id
        self.__b_name = b_name
        self.__b_author = b_author

        print ("The ID of the Book is ", self.__b_id)
        print ("The name of the Book is ", self.__b_name)
        print ("The Author of the book is ", self.__b_author)

Book(100,"Harry Potter", "J.K.Rowlin")