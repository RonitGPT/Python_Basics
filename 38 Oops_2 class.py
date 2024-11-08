        # PROGRAM FOR CLASS OBJECT FUNCTION (to give data outside the class )

class Student():

    def getdata(self,id,name,address,grade):
        self.id = id
        self.name = name
        self.address = address
        self.grade = grade

    def display(self):
        print("The id of the student is ", self.id )
        print("The name of the student is ", self.name )
        print("The address of the student is ", self.address )
        print("The grade of the student is ", self.grade )

q = Student()
q.getdata(100,"Yash Katkar","Mumbai","A")
q.display()