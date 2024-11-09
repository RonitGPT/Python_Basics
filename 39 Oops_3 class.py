        # PROGRAM FOR CLASS OBJECT AND FUNCTION (to give data as input from user)

class Student():

    def getdata(self,id,name,address,grade):
        self.id = id
        self.name = name
        self.address = address
        self.grade = grade

    def display (self):
        print("ID is :- ",self.id)
        print("Name is :- ",self.name)
        print("Address is :- ",self.address)
        print("Grade is :- ",self.grade)

s = Student()

id = int(input("Enter the id of the student "))
name = input("Enter the name of the student ")
address = input("Enter the address of the student ")
grade = input("Enter the grade of the student ")

s.getdata(id,name,address,grade)
s.display()