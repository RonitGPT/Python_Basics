        # PROGRAM FOR CLASS OBJECT FUNCTION 

class Student():
    id = 132
    name = "David Smith"
    Address = "Chicago"
    grade = "A grade"

    def getdata(self):
        print("The id of the student is :- ", self.id)
        print("The name of the student is :- ", self.name)
        print("The address of the student is :- ", self.Address)
        print("The grade of the student is :- ", self.grade)

a = Student()
a.getdata()